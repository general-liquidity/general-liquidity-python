# coding: utf-8

"""Cross-language signing parity for the operator surface.

The expected hex signatures are the reference values produced by the TypeScript SDK's
canonicalization + detached ed25519 recipe for a fixed operator key and fixed inputs.
Python, Go, and Rust ports all assert the SAME hex, so the four signers are byte-for-byte
interoperable.
"""

import rfc8785

from general_liquidity.models.amount import Amount
from general_liquidity.models.envelope import Envelope
from general_liquidity.models.grant import Grant
from general_liquidity.models.intent import Intent
from general_liquidity.models.terms import Terms
from general_liquidity.operator import OperatorSigner

SEED_HEX = "0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"
EXPECTED_PUBLIC_KEY = "79b5562e8fe654f94078b112e8a98ba7901f853ae695bed7e0e3910bad049664"
EXPECTED_GRANT_SIG = (
    "b102c754aa024ab55e1f18f85e51a14fc0693d4f1d31daf3a362dd1f72d698eb"
    "4b338b86f3b08105c4bf3d6db8355d6655dad1f1b4c91838afbd135743b80f0a"
)
EXPECTED_INTENT_SIG = (
    "724bd0b4bd9180672e43cb9a91a9a8ae1adf6d5b177451ac049d2c0611fa181b"
    "eb7543698bef0884d2f05cedcd12730a9513f82484731d20634ec40b57177302"
)

AGENT_ID = "agent:acme:007"
MANDATE_ID = "mandate:9f3a"
EXPIRES_AT = "2030-01-01T00:00:00Z"


def signer() -> OperatorSigner:
    return OperatorSigner.from_seed(SEED_HEX)


def test_public_key_matches_reference():
    assert signer().public_key_hex == EXPECTED_PUBLIC_KEY


def test_canonicalization_is_rfc8785_sorted():
    canon = rfc8785.dumps(
        {"agentId": AGENT_ID, "mandateId": MANDATE_ID, "expiresAt": EXPIRES_AT}
    ).decode("utf-8")
    assert canon == (
        '{"agentId":"agent:acme:007",'
        '"expiresAt":"2030-01-01T00:00:00Z",'
        '"mandateId":"mandate:9f3a"}'
    )


def test_sign_grant_matches_ts_reference():
    grant = signer().sign_grant(AGENT_ID, MANDATE_ID, EXPIRES_AT)
    assert isinstance(grant, Grant)
    assert grant.signature == EXPECTED_GRANT_SIG


def test_grant_mandate_delegates_to_sign_grant():
    mandate = Mandate_fixture()
    grant = signer().grant_mandate(mandate, AGENT_ID)
    assert grant.mandate_id == MANDATE_ID
    assert grant.signature == EXPECTED_GRANT_SIG


def test_sign_intent_matches_ts_reference():
    signed = signer().sign_intent(intent_fixture())
    assert signed.envelope.signature == EXPECTED_INTENT_SIG


def Mandate_fixture():
    from general_liquidity.models.mandate import Mandate

    return Mandate(
        id=MANDATE_ID,
        payees=["caip:eip155:1:0xPayee"],
        per_tx_cap=Amount(value="1000000", asset="USDC"),
        per_period_cap=Amount(value="5000000", asset="USDC"),
        period="P1D",
        expires_at=EXPIRES_AT,
    )


def intent_fixture() -> Intent:
    terms = Terms(
        reversibility="irreversible",
        finality="instant",
        credential="eip3009",
        rail="x402",
        capital_source="payer",
        presence="delegated",
    )
    grant = Grant(
        agent_id=AGENT_ID,
        mandate_id=MANDATE_ID,
        expires_at=EXPIRES_AT,
        signature="g",
    )
    envelope = Envelope(
        identity=AGENT_ID, mandate_id=MANDATE_ID, grant=grant, signature=""
    )
    return Intent(
        idempotency_key="invoice-42-key",
        payee="caip:eip155:1:0xPayee",
        amount=Amount(value="1000000", asset="USDC"),
        purpose="invoice-42",
        terms=terms,
        envelope=envelope,
    )
