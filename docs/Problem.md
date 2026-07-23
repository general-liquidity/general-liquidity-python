# Problem

RFC 7807 problem detail. For an agent the error IS the recovery instruction: `code` is a stable machine token to branch on and `retry_after` is a valid-retry hint. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference identifying the problem type. | [default to 'about:blank']
**title** | **str** | Short, human-readable summary of the problem type. | 
**status** | **int** | HTTP status code. | 
**detail** | **str** | Human-readable explanation specific to this occurrence. | [optional] 
**instance** | **str** |  | [optional] 
**code** | **str** | Stable machine code an agent branches on, e.g. \&quot;over_mandate\&quot; | \&quot;rate_limited\&quot;. The memory group adds: \&quot;memory.denied\&quot; (403, engine refused a gated write), \&quot;memory.forbidden\&quot; (403, mandate scope/capability refusal), and \&quot;memory.pending\&quot; (202, write parked for operator confirmation).  | [optional] 
**retry_after** | **int** | Valid-retry hint in seconds; absent when the call must not be retried as-is. | [optional] 

## Example

```python
from general_liquidity.models.problem import Problem

# TODO update the JSON string below
json = "{}"
# create an instance of Problem from a JSON string
problem_instance = Problem.from_json(json)
# print the JSON string representation of the object
print(Problem.to_json())

# convert the object into a dict
problem_dict = problem_instance.to_dict()
# create an instance of Problem from a dict
problem_from_dict = Problem.from_dict(problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


