# AuditEvent

A single signed, hash-linked entry in the audit trail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Monotonic wire event type, e.g. \&quot;intent.gated\&quot; | \&quot;intent.settled\&quot;. | 
**at** | **datetime** |  | 
**intent_key** | **str** |  | [optional] 
**prev** | **str** | HMAC hash of the previous entry — the hash-link. | [optional] 
**payload** | **object** |  | 

## Example

```python
from general_liquidity.models.audit_event import AuditEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEvent from a JSON string
audit_event_instance = AuditEvent.from_json(json)
# print the JSON string representation of the object
print(AuditEvent.to_json())

# convert the object into a dict
audit_event_dict = audit_event_instance.to_dict()
# create an instance of AuditEvent from a dict
audit_event_from_dict = AuditEvent.from_dict(audit_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


