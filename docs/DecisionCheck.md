# DecisionCheck

One policy predicate the gate evaluated, named by a stable id. Unlike `reasons`, which is prose for a human, a check is safe to persist, compare across versions and switch on. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**passed** | **bool** |  | 

## Example

```python
from general_liquidity.models.decision_check import DecisionCheck

# TODO update the JSON string below
json = "{}"
# create an instance of DecisionCheck from a JSON string
decision_check_instance = DecisionCheck.from_json(json)
# print the JSON string representation of the object
print(DecisionCheck.to_json())

# convert the object into a dict
decision_check_dict = decision_check_instance.to_dict()
# create an instance of DecisionCheck from a dict
decision_check_from_dict = DecisionCheck.from_dict(decision_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


