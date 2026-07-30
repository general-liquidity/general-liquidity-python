# BuyRequest

The quote fields plus the mandate-bearing envelope and terms the authorize beat needs — the same envelope `/pay` carries, because the same gate evaluates it. No amount appears: the price is the merchant's, taken from the server-authoritative cart. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** | Client-generated, server-enforced replay key, carried in the BODY (not the header) and namespaced apart from &#x60;/pay&#x60;&#39;s. Stripped before the request reaches the checkout engine: the intent the gate evaluates is keyed on the merchant&#39;s own cart id.  | 
**rail** | **str** | The checkout protocol to dispatch to. | 
**merchant** | **str** |  | 
**currency** | **str** |  | 
**lines** | [**List[CommerceLine]**](CommerceLine.md) |  | 
**purpose** | **str** | What the purchase is for. Evaluated by the gate, as on &#x60;/pay&#x60;. | 
**terms** | [**Terms**](Terms.md) |  | 
**envelope** | [**Envelope**](Envelope.md) |  | 

## Example

```python
from general_liquidity.models.buy_request import BuyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyRequest from a JSON string
buy_request_instance = BuyRequest.from_json(json)
# print the JSON string representation of the object
print(BuyRequest.to_json())

# convert the object into a dict
buy_request_dict = buy_request_instance.to_dict()
# create an instance of BuyRequest from a dict
buy_request_from_dict = BuyRequest.from_dict(buy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


