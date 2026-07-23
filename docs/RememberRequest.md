# RememberRequest

A gated memory write. The mandate needs `canWrite`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate** | [**MemoryMandate**](MemoryMandate.md) |  | 
**body** | **object** |  | [optional] 
**valid_from** | **datetime** |  | 
**valid_to** | **datetime** |  | 
**edges** | [**List[RememberRequestEdgesInner]**](RememberRequestEdgesInner.md) |  | [optional] 
**source** | **str** |  | 

## Example

```python
from general_liquidity.models.remember_request import RememberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RememberRequest from a JSON string
remember_request_instance = RememberRequest.from_json(json)
# print the JSON string representation of the object
print(RememberRequest.to_json())

# convert the object into a dict
remember_request_dict = remember_request_instance.to_dict()
# create an instance of RememberRequest from a dict
remember_request_from_dict = RememberRequest.from_dict(remember_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


