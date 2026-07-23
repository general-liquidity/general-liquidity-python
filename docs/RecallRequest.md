# RecallRequest

A point-in-time read. The mandate needs `canRead`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate** | [**MemoryMandate**](MemoryMandate.md) |  | 
**valid_at** | **datetime** |  | 
**tx_at** | **datetime** |  | 
**namespace** | **str** |  | [optional] 

## Example

```python
from general_liquidity.models.recall_request import RecallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecallRequest from a JSON string
recall_request_instance = RecallRequest.from_json(json)
# print the JSON string representation of the object
print(RecallRequest.to_json())

# convert the object into a dict
recall_request_dict = recall_request_instance.to_dict()
# create an instance of RecallRequest from a dict
recall_request_from_dict = RecallRequest.from_dict(recall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


