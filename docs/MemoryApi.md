# general_liquidity.MemoryApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memory_assemble**](MemoryApi.md#memory_assemble) | **POST** /memory/assemble | Assemble a budgeted, signed context from a snapshot.
[**memory_forget**](MemoryApi.md#memory_forget) | **POST** /memory/forget | Cascading erasure of a record and its dependents. (Operator)
[**memory_recall**](MemoryApi.md#memory_recall) | **POST** /memory/recall | Read a sealed point-in-time snapshot.
[**memory_remember**](MemoryApi.md#memory_remember) | **POST** /memory/remember | Write one bi-temporal memory record under a mandate.
[**memory_verify**](MemoryApi.md#memory_verify) | **POST** /memory/verify | Verify a signed memory artifact offline.


# **memory_assemble**
> AssembledContext memory_assemble(assemble_request)

Assemble a budgeted, signed context from a snapshot.

Take a supplied `snapshot` (or `recall` params to produce one) and return a signed `AssembledContext` within `budget.maxTokens`. Needs `canRead`. Abstention (the engine declining to fill the budget) is a valid `200`, not an error. Default-off: 404 absent an engine. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.assemble_request import AssembleRequest
from general_liquidity.models.assembled_context import AssembledContext
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
    api_instance = general_liquidity.MemoryApi(api_client)
    assemble_request = general_liquidity.AssembleRequest() # AssembleRequest | 

    try:
        # Assemble a budgeted, signed context from a snapshot.
        api_response = api_instance.memory_assemble(assemble_request)
        print("The response of MemoryApi->memory_assemble:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_assemble: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assemble_request** | [**AssembleRequest**](AssembleRequest.md)|  | 

### Return type

[**AssembledContext**](AssembledContext.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signed, ordered context (possibly an abstention). |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memory_forget**
> ErasureProof memory_forget(forget_request)

Cascading erasure of a record and its dependents. (Operator)

DESTRUCTIVE and OPERATOR-privileged: gated by the `GL-Operator` credential on its own disjoint domain (the same channel the kill switch + webhook CRUD use), never the agent bearer token, so an agent credential grants nothing here. The mandate's `canErase` is checked in ADDITION. Returns a signed `ErasureProof` and emits `memory.erased`. Default-off: 404 absent a memory engine. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.erasure_proof import ErasureProof
from general_liquidity.models.forget_request import ForgetRequest
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

# Configure API key authorization: operatorAuth
configuration.api_key['operatorAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['operatorAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with general_liquidity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_liquidity.MemoryApi(api_client)
    forget_request = general_liquidity.ForgetRequest() # ForgetRequest | 

    try:
        # Cascading erasure of a record and its dependents. (Operator)
        api_response = api_instance.memory_forget(forget_request)
        print("The response of MemoryApi->memory_forget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_forget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forget_request** | [**ForgetRequest**](ForgetRequest.md)|  | 

### Return type

[**ErasureProof**](ErasureProof.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signed cascading-erasure proof. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memory_recall**
> SnapshotPage memory_recall(recall_request)

Read a sealed point-in-time snapshot.

Read the records valid at `validAt` as known at `txAt`, under one seal, cursor-paginated for large snapshots. Needs `canRead`; a recall reaching before the mandate's `asOfFloor` is a `memory.forbidden`. Default-off: absent a memory engine, this is a 404. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.recall_request import RecallRequest
from general_liquidity.models.snapshot_page import SnapshotPage
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
    api_instance = general_liquidity.MemoryApi(api_client)
    recall_request = general_liquidity.RecallRequest() # RecallRequest | 

    try:
        # Read a sealed point-in-time snapshot.
        api_response = api_instance.memory_recall(recall_request)
        print("The response of MemoryApi->memory_recall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_recall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recall_request** | [**RecallRequest**](RecallRequest.md)|  | 

### Return type

[**SnapshotPage**](SnapshotPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of snapshot records carrying the full-snapshot seal + coordinates. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memory_remember**
> MemoryRecord memory_remember(remember_request)

Write one bi-temporal memory record under a mandate.

Write a record valid from `validFrom` (open-ended when `validTo` is null). The engine gates the write against the `MemoryMandate` (needs `canWrite`) and its own preconditions: `allow` returns the signed `MemoryRecord`; a parked write is a `202 memory.pending`; a refusal is `memory.denied` (engine) or `memory.forbidden` (mandate). No-lookahead: a record never reveals a future edit. Default-off: absent a memory engine, this is a 404. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.memory_record import MemoryRecord
from general_liquidity.models.remember_request import RememberRequest
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
    api_instance = general_liquidity.MemoryApi(api_client)
    remember_request = general_liquidity.RememberRequest() # RememberRequest | 

    try:
        # Write one bi-temporal memory record under a mandate.
        api_response = api_instance.memory_remember(remember_request)
        print("The response of MemoryApi->memory_remember:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_remember: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remember_request** | [**RememberRequest**](RememberRequest.md)|  | 

### Return type

[**MemoryRecord**](MemoryRecord.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signed, recorded bi-temporal record. |  -  |
**202** | The write was accepted and parked pending operator confirmation. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memory_verify**
> MemoryVerify200Response memory_verify(memory_verify_request)

Verify a signed memory artifact offline.

Offline verification of a signed record · snapshot · context · erasure proof. FREE and UNMETERED: it reaches no store, mutates nothing, and needs no mandate. Default-off: 404 absent a memory engine. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.memory_verify200_response import MemoryVerify200Response
from general_liquidity.models.memory_verify_request import MemoryVerifyRequest
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
    api_instance = general_liquidity.MemoryApi(api_client)
    memory_verify_request = general_liquidity.MemoryVerifyRequest() # MemoryVerifyRequest | 

    try:
        # Verify a signed memory artifact offline.
        api_response = api_instance.memory_verify(memory_verify_request)
        print("The response of MemoryApi->memory_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_verify_request** | [**MemoryVerifyRequest**](MemoryVerifyRequest.md)|  | 

### Return type

[**MemoryVerify200Response**](MemoryVerify200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The verification verdict. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

