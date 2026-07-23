# MemoryVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **object** | A signed memory artifact to verify. | 

## Example

```python
from general_liquidity.models.memory_verify_request import MemoryVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryVerifyRequest from a JSON string
memory_verify_request_instance = MemoryVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(MemoryVerifyRequest.to_json())

# convert the object into a dict
memory_verify_request_dict = memory_verify_request_instance.to_dict()
# create an instance of MemoryVerifyRequest from a dict
memory_verify_request_from_dict = MemoryVerifyRequest.from_dict(memory_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


