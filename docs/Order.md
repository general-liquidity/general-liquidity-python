# Order

A completed purchase, as `buy` returns it. The merchant stays merchant-of-record; GL supplied the gated settlement and the receipt that proves it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**cart_id** | **str** | The cart this order was placed from. | 
**protocol** | **str** |  | 
**status** | [**CartStatus**](CartStatus.md) |  | 
**merchant** | **str** |  | 
**receipt** | [**Receipt**](Receipt.md) | The settlement Receipt the gated &#x60;pay&#x60; produced for the authorize beat. | 
**placed_at** | **datetime** |  | 

## Example

```python
from general_liquidity.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


