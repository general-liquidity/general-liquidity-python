# Receipt

Durable, machine-parseable proof of settlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent_key** | **str** |  | 
**rail** | [**RailId**](RailId.md) |  | 
**reference** | **str** | Rail settlement reference / on-chain tx hash. | 
**terms** | [**Terms**](Terms.md) |  | 
**settled_at** | **datetime** |  | 
**enforcement** | **str** | Proof-of-Enforcement hash, byte-identical between emitter and verifier. | 

## Example

```python
from general_liquidity.models.receipt import Receipt

# TODO update the JSON string below
json = "{}"
# create an instance of Receipt from a JSON string
receipt_instance = Receipt.from_json(json)
# print the JSON string representation of the object
print(Receipt.to_json())

# convert the object into a dict
receipt_dict = receipt_instance.to_dict()
# create an instance of Receipt from a dict
receipt_from_dict = Receipt.from_dict(receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


