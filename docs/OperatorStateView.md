# OperatorStateView

The live halt state, returned so an operator sees the effect of what they just did.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kill_switch_engaged** | **bool** |  | 
**circuit_breaker_open** | **bool** |  | 

## Example

```python
from general_liquidity.models.operator_state_view import OperatorStateView

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorStateView from a JSON string
operator_state_view_instance = OperatorStateView.from_json(json)
# print the JSON string representation of the object
print(OperatorStateView.to_json())

# convert the object into a dict
operator_state_view_dict = operator_state_view_instance.to_dict()
# create an instance of OperatorStateView from a dict
operator_state_view_from_dict = OperatorStateView.from_dict(operator_state_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


