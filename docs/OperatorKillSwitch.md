# OperatorKillSwitch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engaged** | **bool** | True freezes the settle path; false releases it. Signed separately per direction. | 
**rationale** | **str** |  | 

## Example

```python
from general_liquidity.models.operator_kill_switch import OperatorKillSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorKillSwitch from a JSON string
operator_kill_switch_instance = OperatorKillSwitch.from_json(json)
# print the JSON string representation of the object
print(OperatorKillSwitch.to_json())

# convert the object into a dict
operator_kill_switch_dict = operator_kill_switch_instance.to_dict()
# create an instance of OperatorKillSwitch from a dict
operator_kill_switch_from_dict = OperatorKillSwitch.from_dict(operator_kill_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


