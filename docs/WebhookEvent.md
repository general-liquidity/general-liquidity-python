# WebhookEvent

One delivered webhook event, derived from a signed audit entry. `id` is deterministic in the source entry (dedup key across at-least-once retries). Signed with the endpoint's secret via the `GL-Signature` header. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deterministic event id, &#x60;evt_&lt;audit_hash&gt;&#x60;. | 
**type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**created_at** | **datetime** |  | 
**data** | **Dict[str, object]** | The source entry&#39;s payload plus the chain coordinates (&#x60;audit_seq&#x60;, &#x60;audit_hash&#x60;, &#x60;audit_type&#x60;) that let a consumer re-verify the underlying signed audit entry. For &#x60;payment.settled&#x60; a Receipt-shaped record; for &#x60;intent.denied&#x60; / &#x60;approval.pending&#x60; the gate Decision; for &#x60;audit.appended&#x60; the whole AuditEvent.  | 

## Example

```python
from general_liquidity.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


