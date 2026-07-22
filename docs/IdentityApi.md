# general_liquidity.IdentityApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disclose**](IdentityApi.md#disclose) | **POST** /disclose | Produce GL&#39;s own signed disclosure.
[**resolve**](IdentityApi.md#resolve) | **POST** /resolve | Normalize any counterparty reference into one identity.
[**verify**](IdentityApi.md#verify) | **POST** /verify | Check a counterparty&#39;s signed disclosure against policy.


# **disclose**
> Disclosure disclose()

Produce GL's own signed disclosure.

Produce GL's own signed `Disclosure`: what this agent is and what it is authorized to do. Read-only with respect to value. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.disclosure import Disclosure
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
    api_instance = general_liquidity.IdentityApi(api_client)

    try:
        # Produce GL's own signed disclosure.
        api_response = api_instance.disclose()
        print("The response of IdentityApi->disclose:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->disclose: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Disclosure**](Disclosure.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signed self-description. |  -  |
**401** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve**
> Counterparty resolve(resolve_request)

Normalize any counterparty reference into one identity.

Normalize a counterparty reference (A2A card · signed disclosure · CAIP account) into one identity, its accepted rails, and trust signals. Read-only. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.counterparty import Counterparty
from general_liquidity.models.resolve_request import ResolveRequest
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
    api_instance = general_liquidity.IdentityApi(api_client)
    resolve_request = general_liquidity.ResolveRequest() # ResolveRequest | 

    try:
        # Normalize any counterparty reference into one identity.
        api_response = api_instance.resolve(resolve_request)
        print("The response of IdentityApi->resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolve_request** | [**ResolveRequest**](ResolveRequest.md)|  | 

### Return type

[**Counterparty**](Counterparty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The normalized counterparty. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> Decision verify(disclosure)

Check a counterparty's signed disclosure against policy.

Check a counterparty's signed `Disclosure` against policy — identity, provenance, and enforcement proof — returning a `Decision`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.decision import Decision
from general_liquidity.models.disclosure import Disclosure
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
    api_instance = general_liquidity.IdentityApi(api_client)
    disclosure = general_liquidity.Disclosure() # Disclosure | 

    try:
        # Check a counterparty's signed disclosure against policy.
        api_response = api_instance.verify(disclosure)
        print("The response of IdentityApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disclosure** | [**Disclosure**](Disclosure.md)|  | 

### Return type

[**Decision**](Decision.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gate&#39;s decision on the disclosure. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

