# UpdateWebhookEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from general_liquidity.models.update_webhook_endpoint_request import UpdateWebhookEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookEndpointRequest from a JSON string
update_webhook_endpoint_request_instance = UpdateWebhookEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookEndpointRequest.to_json())

# convert the object into a dict
update_webhook_endpoint_request_dict = update_webhook_endpoint_request_instance.to_dict()
# create an instance of UpdateWebhookEndpointRequest from a dict
update_webhook_endpoint_request_from_dict = UpdateWebhookEndpointRequest.from_dict(update_webhook_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


