# MemoryMandate

Scopes an agent's memory authority — the memory analog of the spend mandate. `asOfFloor` bounds how far back a recall may reach (a recall `validAt` earlier than it is refused). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | 
**can_read** | **bool** |  | 
**can_write** | **bool** |  | 
**can_erase** | **bool** |  | 
**as_of_floor** | **datetime** |  | [optional] 

## Example

```python
from general_liquidity.models.memory_mandate import MemoryMandate

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryMandate from a JSON string
memory_mandate_instance = MemoryMandate.from_json(json)
# print the JSON string representation of the object
print(MemoryMandate.to_json())

# convert the object into a dict
memory_mandate_dict = memory_mandate_instance.to_dict()
# create an instance of MemoryMandate from a dict
memory_mandate_from_dict = MemoryMandate.from_dict(memory_mandate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


