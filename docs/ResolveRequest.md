# ResolveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A2A card URL, signed disclosure id, or CAIP-10 account. | 

## Example

```python
from general_liquidity.models.resolve_request import ResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveRequest from a JSON string
resolve_request_instance = ResolveRequest.from_json(json)
# print the JSON string representation of the object
print(ResolveRequest.to_json())

# convert the object into a dict
resolve_request_dict = resolve_request_instance.to_dict()
# create an instance of ResolveRequest from a dict
resolve_request_from_dict = ResolveRequest.from_dict(resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


