# Audit200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditEvent]**](AuditEvent.md) |  | 
**has_more** | **bool** | True when items remain after this page. | 
**next_cursor** | **str** | Token for the next page, or null when &#x60;has_more&#x60; is false. | 

## Example

```python
from general_liquidity.models.audit200_response import Audit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Audit200Response from a JSON string
audit200_response_instance = Audit200Response.from_json(json)
# print the JSON string representation of the object
print(Audit200Response.to_json())

# convert the object into a dict
audit200_response_dict = audit200_response_instance.to_dict()
# create an instance of Audit200Response from a dict
audit200_response_from_dict = Audit200Response.from_dict(audit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


