# Proof

A falsifiable Proof-of-Enforcement record binding authorization scope to execution outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_hash** | **str** | Byte-identical between the enforcement emitter and the independent verifier. | 
**intent_key** | **str** |  | 
**verified** | **bool** |  | [optional] 

## Example

```python
from general_liquidity.models.proof import Proof

# TODO update the JSON string below
json = "{}"
# create an instance of Proof from a JSON string
proof_instance = Proof.from_json(json)
# print the JSON string representation of the object
print(Proof.to_json())

# convert the object into a dict
proof_dict = proof_instance.to_dict()
# create an instance of Proof from a dict
proof_from_dict = Proof.from_dict(proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


