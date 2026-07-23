# Pay202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**Outcome**](Outcome.md) |  | 
**reasons** | **List[str]** |  | 
**mandate_id** | **str** |  | 
**type** | **str** |  | 
**title** | **str** |  | 
**obligation_id** | **str** | The obligation the spend is conditional on. | 
**state** | **str** |  | 
**awaiting** | [**EvidenceClass**](EvidenceClass.md) | The admissibility class still awaited before the spend can settle. | 
**achieved_class** | [**EvidenceClass**](EvidenceClass.md) | The strongest class the admitted evidence has reached so far. | [optional] 

## Example

```python
from general_liquidity.models.pay202_response import Pay202Response

# TODO update the JSON string below
json = "{}"
# create an instance of Pay202Response from a JSON string
pay202_response_instance = Pay202Response.from_json(json)
# print the JSON string representation of the object
print(Pay202Response.to_json())

# convert the object into a dict
pay202_response_dict = pay202_response_instance.to_dict()
# create an instance of Pay202Response from a dict
pay202_response_from_dict = Pay202Response.from_dict(pay202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


