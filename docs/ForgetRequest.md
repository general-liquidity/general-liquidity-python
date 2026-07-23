# ForgetRequest

Cascading erasure of a root and its dependents. Operator-privileged; needs `canErase`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate** | [**MemoryMandate**](MemoryMandate.md) |  | 
**root_id** | **str** |  | 

## Example

```python
from general_liquidity.models.forget_request import ForgetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForgetRequest from a JSON string
forget_request_instance = ForgetRequest.from_json(json)
# print the JSON string representation of the object
print(ForgetRequest.to_json())

# convert the object into a dict
forget_request_dict = forget_request_instance.to_dict()
# create an instance of ForgetRequest from a dict
forget_request_from_dict = ForgetRequest.from_dict(forget_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


