# JobPending

Resume material, present only on a pending job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate_id** | **str** |  | [optional] 
**challenge** | **str** | Opaque challenge an operator approval binds to. | [optional] 

## Example

```python
from general_liquidity.models.job_pending import JobPending

# TODO update the JSON string below
json = "{}"
# create an instance of JobPending from a JSON string
job_pending_instance = JobPending.from_json(json)
# print the JSON string representation of the object
print(JobPending.to_json())

# convert the object into a dict
job_pending_dict = job_pending_instance.to_dict()
# create an instance of JobPending from a dict
job_pending_from_dict = JobPending.from_dict(job_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


