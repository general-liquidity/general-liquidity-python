# OperatorRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent_id** | **str** |  | 
**amount_minor** | **int** | Minor units to refund. Omitted, the full outstanding amount. | [optional] 
**rationale** | **str** |  | 

## Example

```python
from general_liquidity.models.operator_refund import OperatorRefund

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorRefund from a JSON string
operator_refund_instance = OperatorRefund.from_json(json)
# print the JSON string representation of the object
print(OperatorRefund.to_json())

# convert the object into a dict
operator_refund_dict = operator_refund_instance.to_dict()
# create an instance of OperatorRefund from a dict
operator_refund_from_dict = OperatorRefund.from_dict(operator_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


