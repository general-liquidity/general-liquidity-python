# Intent

A signed request to move value. Input to pay(); never carries a settle primitive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** |  | 
**payee** | **str** | Resolved to a CAIP-10 account where the rail is on-chain. | 
**amount** | [**Amount**](Amount.md) |  | 
**purpose** | **str** |  | 
**terms** | [**Terms**](Terms.md) |  | 
**envelope** | [**Envelope**](Envelope.md) |  | 

## Example

```python
from general_liquidity.models.intent import Intent

# TODO update the JSON string below
json = "{}"
# create an instance of Intent from a JSON string
intent_instance = Intent.from_json(json)
# print the JSON string representation of the object
print(Intent.to_json())

# convert the object into a dict
intent_dict = intent_instance.to_dict()
# create an instance of Intent from a dict
intent_from_dict = Intent.from_dict(intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


