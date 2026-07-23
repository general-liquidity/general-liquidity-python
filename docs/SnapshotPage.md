# SnapshotPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MemoryRecord]**](MemoryRecord.md) |  | 
**has_more** | **bool** | True when items remain after this page. | 
**next_cursor** | **str** | Token for the next page, or null when &#x60;has_more&#x60; is false. | 
**valid_at** | **datetime** |  | 
**tx_at** | **datetime** |  | 
**seal** | [**Seal**](Seal.md) |  | 

## Example

```python
from general_liquidity.models.snapshot_page import SnapshotPage

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotPage from a JSON string
snapshot_page_instance = SnapshotPage.from_json(json)
# print the JSON string representation of the object
print(SnapshotPage.to_json())

# convert the object into a dict
snapshot_page_dict = snapshot_page_instance.to_dict()
# create an instance of SnapshotPage from a dict
snapshot_page_from_dict = SnapshotPage.from_dict(snapshot_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


