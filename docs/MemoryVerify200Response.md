# MemoryVerify200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from general_liquidity.models.memory_verify200_response import MemoryVerify200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryVerify200Response from a JSON string
memory_verify200_response_instance = MemoryVerify200Response.from_json(json)
# print the JSON string representation of the object
print(MemoryVerify200Response.to_json())

# convert the object into a dict
memory_verify200_response_dict = memory_verify200_response_instance.to_dict()
# create an instance of MemoryVerify200Response from a dict
memory_verify200_response_from_dict = MemoryVerify200Response.from_dict(memory_verify200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


