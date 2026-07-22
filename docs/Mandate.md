# Mandate

Operator-granted, scoped, capped, expiring spend authority.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**payees** | **List[str]** | Allowed counterparties (CAIP-10 where on-chain). | 
**per_tx_cap** | [**Amount**](Amount.md) |  | 
**per_period_cap** | [**Amount**](Amount.md) |  | 
**period** | **str** | ISO-8601 duration for the period cap window. | 
**expires_at** | **datetime** |  | 
**constraints** | **Dict[str, object]** |  | [optional] 

## Example

```python
from general_liquidity.models.mandate import Mandate

# TODO update the JSON string below
json = "{}"
# create an instance of Mandate from a JSON string
mandate_instance = Mandate.from_json(json)
# print the JSON string representation of the object
print(Mandate.to_json())

# convert the object into a dict
mandate_dict = mandate_instance.to_dict()
# create an instance of Mandate from a dict
mandate_from_dict = Mandate.from_dict(mandate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


