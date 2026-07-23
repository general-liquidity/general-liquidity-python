# general_liquidity.GovernanceApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit**](GovernanceApi.md#audit) | **GET** /audit | Read the signed, hash-linked audit trail (cursor-paginated).
[**audit_stream**](GovernanceApi.md#audit_stream) | **GET** /audit/stream | Subscribe to the signed audit chain as Server-Sent Events.
[**get_intent**](GovernanceApi.md#get_intent) | **GET** /intents/{id} | Read the async job resource for one intent.
[**get_intent_events**](GovernanceApi.md#get_intent_events) | **GET** /intents/{id}/events | List one intent&#39;s audit events (cursor-paginated).
[**get_usage**](GovernanceApi.md#get_usage) | **GET** /usage | Read metered call counts for the authenticated principal.


# **audit**
> Audit200Response audit(cursor=cursor, limit=limit)

Read the signed, hash-linked audit trail (cursor-paginated).

Returns a `Page` envelope of signed audit events, keyed on the audit `seq`. Pass `cursor` (from a prior page's `next_cursor`) to resume; a `limit`-only call with no cursor returns the first page, so the legacy bare-`limit` request keeps working. A malformed or stale cursor is a `400 intent.malformed`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.audit200_response import Audit200Response
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
    cursor = 'cursor_example' # str | Opaque token from a prior page's `next_cursor`. Absent means \"from the start\". (optional)
    limit = 20 # int | Page size, clamped to [1, 100]; defaults to 20. (optional) (default to 20)

    try:
        # Read the signed, hash-linked audit trail (cursor-paginated).
        api_response = api_instance.audit(cursor=cursor, limit=limit)
        print("The response of GovernanceApi->audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->audit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque token from a prior page&#39;s &#x60;next_cursor&#x60;. Absent means \&quot;from the start\&quot;. | [optional] 
 **limit** | **int**| Page size, clamped to [1, 100]; defaults to 20. | [optional] [default to 20]

### Return type

[**Audit200Response**](Audit200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of signed audit events. |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Request-Id -  <br>  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audit_stream**
> str audit_stream(last_event_id=last_event_id)

Subscribe to the signed audit chain as Server-Sent Events.

A read/observe surface over the SAME signed audit chain `/audit` pages. Returns a `text/event-stream`: each appended entry is one SSE frame (`id:` = the audit `seq`, `event:` = the entry type, `data:` = the entry). A reconnecting client sends `Last-Event-ID` (the last `seq` it saw) to replay missed entries before joining the live fan-out. Never moves money and never writes the chain. Default-off: absent an event-stream backing, this route is a 404. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
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
    last_event_id = 'last_event_id_example' # str | The last audit `seq` the client received, for gap-free resume. (optional)

    try:
        # Subscribe to the signed audit chain as Server-Sent Events.
        api_response = api_instance.audit_stream(last_event_id=last_event_id)
        print("The response of GovernanceApi->audit_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->audit_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_event_id** | **str**| The last audit &#x60;seq&#x60; the client received, for gap-free resume. | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An open SSE stream of audit entries. |  * X-Request-Id -  <br>  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intent**
> Job get_intent(id)

Read the async job resource for one intent.

A first-class read projection over an intent's confirm-park-approve lifecycle: a stable id, a terminal-state enum, the settlement receipt on a settled job, the RFC 9457 problem on a denied/failed job, and the resume material (challenge + mandate) on a still-pending job. Derived from the persisted intent + the signed audit trail. Default-off: absent the job wiring, this route is a 404. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.job import Job
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
    id = 'id_example' # str | The intent's idempotency key — the stable resource id.

    try:
        # Read the async job resource for one intent.
        api_response = api_instance.get_intent(id)
        print("The response of GovernanceApi->get_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->get_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The intent&#39;s idempotency key — the stable resource id. | 

### Return type

[**Job**](Job.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job resource. |  * X-Request-Id -  <br>  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intent_events**
> Audit200Response get_intent_events(id, cursor=cursor, limit=limit)

List one intent's audit events (cursor-paginated).

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.audit200_response import Audit200Response
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
    id = 'id_example' # str | 
    cursor = 'cursor_example' # str | Opaque token from a prior page's `next_cursor`. Absent means \"from the start\". (optional)
    limit = 20 # int | Page size, clamped to [1, 100]; defaults to 20. (optional) (default to 20)

    try:
        # List one intent's audit events (cursor-paginated).
        api_response = api_instance.get_intent_events(id, cursor=cursor, limit=limit)
        print("The response of GovernanceApi->get_intent_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->get_intent_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cursor** | **str**| Opaque token from a prior page&#39;s &#x60;next_cursor&#x60;. Absent means \&quot;from the start\&quot;. | [optional] 
 **limit** | **int**| Page size, clamped to [1, 100]; defaults to 20. | [optional] [default to 20]

### Return type

[**Audit200Response**](Audit200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of the intent&#39;s signed audit events. |  * X-Request-Id -  <br>  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> UsageSummary get_usage(since, until, tags=tags)

Read metered call counts for the authenticated principal.

Call counting only — no prices, no billing. Aggregates the authenticated principal's calls over a half-open window `[since, until)`, optionally filtered to calls carrying EVERY listed tag (AND semantics). Tags are UNSIGNED per-request attribution supplied via the `X-GL-Tags` header; they never touch the Intent or the gate decision. Default-off: absent a usage store, this route is a 404 and nothing is recorded. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.usage_summary import UsageSummary
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
    since = '2013-10-20T19:20:30+01:00' # datetime | ISO-8601 inclusive lower bound.
    until = '2013-10-20T19:20:30+01:00' # datetime | ISO-8601 exclusive upper bound.
    tags = ['tags_example'] # List[str] | Repeatable; count only calls carrying every listed tag. (optional)

    try:
        # Read metered call counts for the authenticated principal.
        api_response = api_instance.get_usage(since, until, tags=tags)
        print("The response of GovernanceApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->get_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| ISO-8601 inclusive lower bound. | 
 **until** | **datetime**| ISO-8601 exclusive upper bound. | 
 **tags** | [**List[str]**](str.md)| Repeatable; count only calls carrying every listed tag. | [optional] 

### Return type

[**UsageSummary**](UsageSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The usage summary. |  * X-Request-Id -  <br>  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

