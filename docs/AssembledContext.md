# AssembledContext

A budgeted, ordered context assembled from a snapshot, under one seal. Abstention (`abstained: true`) is a valid result — the engine declining to fill the budget. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[MemoryRecord]**](MemoryRecord.md) |  | 
**order** | **List[str]** |  | 
**budget** | [**AssembledContextBudget**](AssembledContextBudget.md) |  | 
**abstained** | **bool** |  | 
**abstain_reason** | **str** |  | [optional] 
**seal** | [**Seal**](Seal.md) |  | 

## Example

```python
from general_liquidity.models.assembled_context import AssembledContext

# TODO update the JSON string below
json = "{}"
# create an instance of AssembledContext from a JSON string
assembled_context_instance = AssembledContext.from_json(json)
# print the JSON string representation of the object
print(AssembledContext.to_json())

# convert the object into a dict
assembled_context_dict = assembled_context_instance.to_dict()
# create an instance of AssembledContext from a dict
assembled_context_from_dict = AssembledContext.from_dict(assembled_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


