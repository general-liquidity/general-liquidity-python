# Job

A read projection over an intent's confirm-park-approve lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The idempotency/intent key — the stable resource id. | 
**status** | [**JobStatus**](JobStatus.md) |  | 
**created_at** | **datetime** | The intent&#39;s first audit entry, falling back to its settle time. | 
**terminal_at** | **datetime** | Set ONLY for terminal states (settled/denied/failed). | [optional] 
**outcome** | [**Outcome**](Outcome.md) |  | 
**receipt** | [**Receipt**](Receipt.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pending** | [**JobPending**](JobPending.md) |  | [optional] 
**links** | [**JobLinks**](JobLinks.md) |  | 

## Example

```python
from general_liquidity.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


