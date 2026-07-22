# General Liquidity Python SDK

The Python client for the General Liquidity machine economy API, generated from the `general-liquidity-openapi` spec.

## Install

Once published:

```bash
pip install general-liquidity
```

From source:

```bash
git clone https://github.com/general-liquidity/general-liquidity-python
cd general-liquidity-python
pip install -e .
```

## Usage

The surface is split into four API classes, each constructed from a shared `ApiClient`:

- `MoneyApi`: `pay`
- `CommerceApi`: `buy`, `quote`
- `IdentityApi`: `resolve`, `disclose`, `verify`
- `GovernanceApi`: `audit`

```python
from general_liquidity import ApiClient, Configuration, MoneyApi
from general_liquidity.models.intent import Intent

config = Configuration(host="https://api.general-liquidity.com")

with ApiClient(config) as api_client:
    money = MoneyApi(api_client)

    intent = Intent.from_dict({
        # ... signed Intent fields per the spec ...
    })

    receipt = money.pay(
        idempotency_key="your-client-generated-key",
        intent=intent,
    )
    print(receipt)
```

`pay` submits a signed `Intent`; the sovereign gate evaluates mandate, caps, risk, velocity, and deny-list, then settles on the routed rail and returns a `Receipt`. The caller never holds a settle primitive. The `idempotency_key` is required on mutating operations (`pay`, `buy`) as a correctness guarantee against double-spend.

Model names (`Intent`, `Receipt`, `Mandate`, `Order`, `QuoteRequest`, `Counterparty`, ...) live under `general_liquidity.models`. See the generated `docs/` directory for the full method and model reference.

## Signing

This generated client covers transport and models only. Intent envelope signing is client-side and is not included here. You are responsible for constructing and signing the `Intent` before passing it to `pay` or `buy`. Only the hand-written TypeScript SDK carries the built-in operator signer today.

## Generation

This SDK is generated from the `general-liquidity-openapi` spec and is regenerated whenever the spec changes. Do not hand-edit the generated modules; change the spec and regenerate.
