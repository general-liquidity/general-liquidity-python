# MemoryRecord

One bi-temporal memory record. `validFrom`/`validTo` are the VALID-time window (the world the fact is about); `recordedAt`/`invalidatedAt` are the TRANSACTION-time window (when the store learned it). No-lookahead: a snapshot at a past instant never reveals a later edit. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**body** | **object** | The arbitrary record payload. | 
**valid_from** | **datetime** |  | 
**valid_to** | **datetime** |  | 
**recorded_at** | **datetime** |  | 
**invalidated_at** | **datetime** |  | 
**edges** | [**List[MemoryRecordEdgesInner]**](MemoryRecordEdgesInner.md) |  | 
**taint** | **bool** |  | 
**source** | **str** |  | 

## Example

```python
from general_liquidity.models.memory_record import MemoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryRecord from a JSON string
memory_record_instance = MemoryRecord.from_json(json)
# print the JSON string representation of the object
print(MemoryRecord.to_json())

# convert the object into a dict
memory_record_dict = memory_record_instance.to_dict()
# create an instance of MemoryRecord from a dict
memory_record_from_dict = MemoryRecord.from_dict(memory_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


