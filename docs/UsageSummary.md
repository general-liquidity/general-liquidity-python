# UsageSummary

Metered call counts for one principal over a half-open window. Counts only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**since** | **datetime** |  | 
**until** | **datetime** |  | 
**total** | **int** | Total calls counted in the window (after any tag filter). | 
**by_operation** | **Dict[str, int]** | Count keyed by operation, e.g. { pay: 3, resolve: 1 }. | 
**by_outcome** | **Dict[str, int]** | Count keyed by outcome, e.g. { allow: 2, deny: 1 }. | 

## Example

```python
from general_liquidity.models.usage_summary import UsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSummary from a JSON string
usage_summary_instance = UsageSummary.from_json(json)
# print the JSON string representation of the object
print(UsageSummary.to_json())

# convert the object into a dict
usage_summary_dict = usage_summary_instance.to_dict()
# create an instance of UsageSummary from a dict
usage_summary_from_dict = UsageSummary.from_dict(usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


