# QuoteRequest

Enough to discover the merchant and price a cart. Every field here is read by the server; nothing else in the body is. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The checkout protocol to dispatch to. Validated against this closed set at the boundary — a &#x60;RailId&#x60; that is not a checkout protocol is refused here, not routed.  | 
**merchant** | **str** | The merchant reference the checkout protocol resolves. | 
**currency** | **str** | The currency the cart is to be priced in. | 
**lines** | [**List[CommerceLine]**](CommerceLine.md) | What to price. Must be non-empty. | 

## Example

```python
from general_liquidity.models.quote_request import QuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequest from a JSON string
quote_request_instance = QuoteRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteRequest.to_json())

# convert the object into a dict
quote_request_dict = quote_request_instance.to_dict()
# create an instance of QuoteRequest from a dict
quote_request_from_dict = QuoteRequest.from_dict(quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


