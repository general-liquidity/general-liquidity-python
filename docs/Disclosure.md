# Disclosure

A signed self-description (identity + provenance). GL's disclosure format. BREAKING CHANGE (version 2026-07-23): collapsed onto the full signed envelope. The prior shape {agent_id, document, signature: string} carried a single key and could not express key rotation; it is replaced by the structured ed25519 signature and an optional rotation_chain. The wire shape now equals the signed envelope both sides exchange, so a rotated signing key can disclose while the stable agent id (document.agentId) is preserved. No agent_id at the top level: it lives in the signed document. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **object** | The signed disclosure document (an AgentDisclosure). Its &#x60;agentId&#x60; field is the stable identity the signature (and any rotation_chain) roots at.  | 
**signature** | [**DisclosureSignature**](DisclosureSignature.md) |  | 
**rotation_chain** | [**List[KeyRotationStatement]**](KeyRotationStatement.md) | Present only when the signing key has rotated away from document.agentId; links the stable id to signature.public_key. Absent in the common no-rotation case.  | [optional] 

## Example

```python
from general_liquidity.models.disclosure import Disclosure

# TODO update the JSON string below
json = "{}"
# create an instance of Disclosure from a JSON string
disclosure_instance = Disclosure.from_json(json)
# print the JSON string representation of the object
print(Disclosure.to_json())

# convert the object into a dict
disclosure_dict = disclosure_instance.to_dict()
# create an instance of Disclosure from a dict
disclosure_from_dict = Disclosure.from_dict(disclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


