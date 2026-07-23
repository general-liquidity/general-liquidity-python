# OperatorApprove

Resume material for a parked intent, exactly as carried on an `approval.pending` problem, plus the operator's rationale and challenge-response acknowledgement. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent_id** | **str** | The parked intent id. | 
**challenge** | **str** | The opaque challenge that binds this approval to that intent. Not a bearer credential. | 
**mandate_id** | **str** | The mandate the gate matched when it parked the intent. | 
**rationale** | **str** | Why the operator is releasing it. Recorded in the signed audit chain. | 
**acknowledged** | **bool** | Explicit challenge-response acknowledgement. Never inferred: a high-risk, irreversible or large intent is not released unless this is &#x60;true&#x60;.  | 

## Example

```python
from general_liquidity.models.operator_approve import OperatorApprove

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorApprove from a JSON string
operator_approve_instance = OperatorApprove.from_json(json)
# print the JSON string representation of the object
print(OperatorApprove.to_json())

# convert the object into a dict
operator_approve_dict = operator_approve_instance.to_dict()
# create an instance of OperatorApprove from a dict
operator_approve_from_dict = OperatorApprove.from_dict(operator_approve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


