# Problem

RFC 9457 problem detail. For an agent the error IS the recovery instruction: `action` is the closed four-value class to branch on, `code` is the stable machine token behind it, and `retryAfter` is a valid-retry hint. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Dereferenceable per-code guidance, &#x60;https://docs.generalliquidity.com/problems/{code}&#x60;. Never &#x60;about:blank&#x60;: an agent that hits an error can fetch the explanation for exactly this code without a human in the loop.  | 
**title** | **str** | Short, human-readable summary of the problem type. | 
**status** | **int** | HTTP status code. | 
**detail** | **str** | Human-readable explanation specific to this occurrence. | 
**code** | **str** | Stable machine code an agent branches on, e.g. \&quot;intent.denied\&quot; | \&quot;rate_limited\&quot;. The memory group adds: \&quot;memory.denied\&quot; (403, engine refused a gated write), \&quot;memory.forbidden\&quot; (403, mandate scope/capability refusal), and \&quot;memory.pending\&quot; (202, write parked for operator confirmation).  | 
**action** | **str** | What the caller should do next. Switch on this, not on &#x60;code&#x60;: new codes arrive over time and a client branching on &#x60;code&#x60; breaks when one does, while these four classes are closed.  | 
**retryable** | **bool** | Derived from &#x60;action&#x60;. Kept so existing clients reading a boolean still work. | 
**retry_after** | **int** | Valid-retry hint in seconds; absent when the call must not be retried as-is. | [optional] 
**reasons** | **List[str]** | Structural context, e.g. the gate&#39;s reasons behind a refusal. | [optional] 
**approval** | [**ProblemApproval**](ProblemApproval.md) |  | [optional] 
**current_state_token** | **str** | Set on &#x60;state.stale&#x60;: the global state token the kernel actually holds. | [optional] 

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


