# general_liquidity.GovernanceApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit**](GovernanceApi.md#audit) | **GET** /audit | Read the signed, hash-linked audit trail.


# **audit**
> List[AuditEvent] audit(intent_key=intent_key, limit=limit)

Read the signed, hash-linked audit trail.

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.audit_event import AuditEvent
from general_liquidity.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.generalliquidity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = general_liquidity.Configuration(
    host = "https://api.generalliquidity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = general_liquidity.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with general_liquidity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_liquidity.GovernanceApi(api_client)
    intent_key = 'intent_key_example' # str | Filter events to a single Intent's idempotency key. (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Read the signed, hash-linked audit trail.
        api_response = api_instance.audit(intent_key=intent_key, limit=limit)
        print("The response of GovernanceApi->audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->audit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intent_key** | **str**| Filter events to a single Intent&#39;s idempotency key. | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[AuditEvent]**](AuditEvent.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of signed audit events. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

