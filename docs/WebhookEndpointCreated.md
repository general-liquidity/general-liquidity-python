# WebhookEndpointCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) |  | 
**active** | **bool** |  | 
**secret** | **str** | The &#x60;whsec_&#x60; HMAC signing secret. Shown ONCE, at create, never again. | 

## Example

```python
from general_liquidity.models.webhook_endpoint_created import WebhookEndpointCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEndpointCreated from a JSON string
webhook_endpoint_created_instance = WebhookEndpointCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookEndpointCreated.to_json())

# convert the object into a dict
webhook_endpoint_created_dict = webhook_endpoint_created_instance.to_dict()
# create an instance of WebhookEndpointCreated from a dict
webhook_endpoint_created_from_dict = WebhookEndpointCreated.from_dict(webhook_endpoint_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


