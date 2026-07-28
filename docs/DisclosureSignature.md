# DisclosureSignature

The ed25519 signature over the canonicalized document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | 
**public_key** | **str** | Signer&#39;s public key (hex). Equals document.agentId in the common case; under rotation it is the current key at the tip of rotationChain.  | 
**value** | **str** | Signature over the canonicalized document (hex). | 

## Example

```python
from general_liquidity.models.disclosure_signature import DisclosureSignature

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureSignature from a JSON string
disclosure_signature_instance = DisclosureSignature.from_json(json)
# print the JSON string representation of the object
print(DisclosureSignature.to_json())

# convert the object into a dict
disclosure_signature_dict = disclosure_signature_instance.to_dict()
# create an instance of DisclosureSignature from a dict
disclosure_signature_from_dict = DisclosureSignature.from_dict(disclosure_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


