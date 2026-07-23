# RefundResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**refunded_minor** | **int** | Cumulative minor units refunded against the intent. | 
**reason** | **str** | Present on refusal, e.g. an irreversible settlement. | [optional] 

## Example

```python
from general_liquidity.models.refund_result import RefundResult

# TODO update the JSON string below
json = "{}"
# create an instance of RefundResult from a JSON string
refund_result_instance = RefundResult.from_json(json)
# print the JSON string representation of the object
print(RefundResult.to_json())

# convert the object into a dict
refund_result_dict = refund_result_instance.to_dict()
# create an instance of RefundResult from a dict
refund_result_from_dict = RefundResult.from_dict(refund_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


