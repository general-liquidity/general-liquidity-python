# AssembleRequest

Budgeted context assembly over a supplied snapshot OR recall params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate** | [**MemoryMandate**](MemoryMandate.md) |  | 
**snapshot** | [**Snapshot**](Snapshot.md) |  | [optional] 
**recall** | [**AssembleRequestRecall**](AssembleRequestRecall.md) |  | [optional] 
**budget** | [**AssembledContextBudget**](AssembledContextBudget.md) |  | 
**namespace** | **str** |  | [optional] 

## Example

```python
from general_liquidity.models.assemble_request import AssembleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssembleRequest from a JSON string
assemble_request_instance = AssembleRequest.from_json(json)
# print the JSON string representation of the object
print(AssembleRequest.to_json())

# convert the object into a dict
assemble_request_dict = assemble_request_instance.to_dict()
# create an instance of AssembleRequest from a dict
assemble_request_from_dict = AssembleRequest.from_dict(assemble_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


