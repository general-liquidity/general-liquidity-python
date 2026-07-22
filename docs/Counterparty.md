# Counterparty

A normalized, resolved identity + accepted rails + trust.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transport** | **str** |  | 
**capabilities** | **List[str]** |  | 
**rails** | [**List[RailId]**](RailId.md) |  | 
**trust** | **object** |  | [optional] 

## Example

```python
from general_liquidity.models.counterparty import Counterparty

# TODO update the JSON string below
json = "{}"
# create an instance of Counterparty from a JSON string
counterparty_instance = Counterparty.from_json(json)
# print the JSON string representation of the object
print(Counterparty.to_json())

# convert the object into a dict
counterparty_dict = counterparty_instance.to_dict()
# create an instance of Counterparty from a dict
counterparty_from_dict = Counterparty.from_dict(counterparty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


