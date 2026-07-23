# coding: utf-8

"""Operator-side signing for General Liquidity.

The operator holds an ed25519 key and counter-signs delegations (a Grant over an
agent+mandate) and Intent envelopes. Keys never leave this process. The signed bytes
are the RFC 8785 (JCS) canonicalization of the camelCase preimage, encoded UTF-8, and
signed with a detached ed25519 signature encoded as lowercase hex. This matches the
reference TypeScript SDK byte-for-byte: the SDK canonicalizes the camelCase domain
object and converts to the snake_case wire form only after signing, so the signed
preimage is camelCase.

Note: the surface exposes no revoke primitive, so none is mirrored here.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Union

import rfc8785
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from general_liquidity.models.grant import Grant
from general_liquidity.models.intent import Intent
from general_liquidity.models.mandate import Mandate


def _canonical_bytes(value: Dict[str, Any]) -> bytes:
    """RFC 8785 JCS canonical bytes of a camelCase preimage."""
    return rfc8785.dumps(value)


def _intent_preimage(intent: Intent) -> Dict[str, Any]:
    """The camelCase preimage the envelope signature is computed over.

    Mirrors the reference SDK: the full Intent with the envelope signature blanked so a
    verifier can recompute it.
    """
    env = intent.envelope
    grant = env.grant
    return {
        "idempotencyKey": intent.idempotency_key,
        "payee": intent.payee,
        "amount": {"value": intent.amount.value, "asset": intent.amount.asset},
        "purpose": intent.purpose,
        "terms": {
            "reversibility": _v(intent.terms.reversibility),
            "finality": _v(intent.terms.finality),
            "credential": intent.terms.credential,
            "rail": _v(intent.terms.rail),
            "capitalSource": _v(intent.terms.capital_source),
            "presence": _v(intent.terms.presence),
        },
        "envelope": {
            "identity": env.identity,
            "mandateId": env.mandate_id,
            "grant": {
                "agentId": grant.agent_id,
                "mandateId": grant.mandate_id,
                "expiresAt": _iso(grant.expires_at),
                "signature": grant.signature,
            },
            "signature": "",
        },
    }


def _v(value: Any) -> Any:
    """Coerce a (str, Enum) member to its underlying wire string."""
    return value.value if isinstance(value, Enum) else value


def _iso(value: Any) -> str:
    """A datetime round-tripped by pydantic must serialize back to its wire string."""
    if isinstance(value, str):
        return value
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


class OperatorSigner:
    """An operator-held ed25519 signer. The private key never leaves this object."""

    def __init__(self, private_key: Ed25519PrivateKey) -> None:
        self._key = private_key

    @classmethod
    def from_seed(cls, seed: Union[bytes, str]) -> "OperatorSigner":
        raw = bytes.fromhex(seed) if isinstance(seed, str) else seed
        return cls(Ed25519PrivateKey.from_private_bytes(raw))

    @property
    def public_key_hex(self) -> str:
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

        return self._key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw).hex()

    @property
    def agent_id(self) -> str:
        return self.public_key_hex

    def _sign(self, preimage: Dict[str, Any]) -> str:
        return self._key.sign(_canonical_bytes(preimage)).hex()

    def sign_grant(self, agent_id: str, mandate_id: str, expires_at: str) -> Grant:
        """Counter-sign a delegation of scope to an agent key.

        Signs over the canonical {agentId, mandateId, expiresAt} and returns the Grant
        carrying the detached hex signature.
        """
        signature = self._sign(
            {"agentId": agent_id, "mandateId": mandate_id, "expiresAt": expires_at}
        )
        return Grant.model_validate(
            {
                "agent_id": agent_id,
                "mandate_id": mandate_id,
                "expires_at": expires_at,
                "signature": signature,
            }
        )

    def grant_mandate(self, mandate: Mandate, agent_id: str) -> Grant:
        """Grant a built Mandate to an agent, returning the counter-signed Grant."""
        return self.sign_grant(agent_id, mandate.id, _iso(mandate.expires_at))

    def sign_intent(self, intent: Intent) -> Intent:
        """Counter-sign an Intent's envelope, returning a copy carrying the signature."""
        signature = self._sign(_intent_preimage(intent))
        signed = intent.model_copy(deep=True)
        signed.envelope.signature = signature
        return signed
