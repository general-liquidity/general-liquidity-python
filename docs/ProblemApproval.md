# ProblemApproval

Set on `approval.pending`: how to resume the parked intent. NONE of this is approval authority; it only names the parked payment. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent_id** | **str** | The parked intent id. | 
**challenge** | **str** | Opaque challenge the approval binds to. Not a bearer credential. | 
**mandate_id** | **str** | The mandate the gate matched, when it matched one. | [optional] 

## Example

```python
from general_liquidity.models.problem_approval import ProblemApproval

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemApproval from a JSON string
problem_approval_instance = ProblemApproval.from_json(json)
# print the JSON string representation of the object
print(ProblemApproval.to_json())

# convert the object into a dict
problem_approval_dict = problem_approval_instance.to_dict()
# create an instance of ProblemApproval from a dict
problem_approval_from_dict = ProblemApproval.from_dict(problem_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


