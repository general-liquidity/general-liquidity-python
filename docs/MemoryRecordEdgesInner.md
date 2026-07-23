# MemoryRecordEdgesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | 
**to** | **str** |  | 

## Example

```python
from general_liquidity.models.memory_record_edges_inner import MemoryRecordEdgesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryRecordEdgesInner from a JSON string
memory_record_edges_inner_instance = MemoryRecordEdgesInner.from_json(json)
# print the JSON string representation of the object
print(MemoryRecordEdgesInner.to_json())

# convert the object into a dict
memory_record_edges_inner_dict = memory_record_edges_inner_instance.to_dict()
# create an instance of MemoryRecordEdgesInner from a dict
memory_record_edges_inner_from_dict = MemoryRecordEdgesInner.from_dict(memory_record_edges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


