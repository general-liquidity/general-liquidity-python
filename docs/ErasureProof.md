# ErasureProof

The signed cascading-erasure proof `forget` returns — the erased ids under a seal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**erased** | **List[str]** |  | 
**proof** | [**Seal**](Seal.md) |  | 

## Example

```python
from general_liquidity.models.erasure_proof import ErasureProof

# TODO update the JSON string below
json = "{}"
# create an instance of ErasureProof from a JSON string
erasure_proof_instance = ErasureProof.from_json(json)
# print the JSON string representation of the object
print(ErasureProof.to_json())

# convert the object into a dict
erasure_proof_dict = erasure_proof_instance.to_dict()
# create an instance of ErasureProof from a dict
erasure_proof_from_dict = ErasureProof.from_dict(erasure_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


