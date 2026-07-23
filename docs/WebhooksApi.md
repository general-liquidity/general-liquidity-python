# general_liquidity.WebhooksApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_endpoint**](WebhooksApi.md#create_webhook_endpoint) | **POST** /webhooks/endpoints | Register a webhook endpoint. (Operator authority)
[**delete_webhook_endpoint**](WebhooksApi.md#delete_webhook_endpoint) | **DELETE** /webhooks/endpoints/{id} | Delete one webhook endpoint. (Operator authority)
[**get_webhook_endpoint**](WebhooksApi.md#get_webhook_endpoint) | **GET** /webhooks/endpoints/{id} | Read one webhook endpoint. (Operator authority)
[**list_webhook_endpoints**](WebhooksApi.md#list_webhook_endpoints) | **GET** /webhooks/endpoints | List webhook endpoints. (Operator authority)
[**update_webhook_endpoint**](WebhooksApi.md#update_webhook_endpoint) | **PATCH** /webhooks/endpoints/{id} | Update one webhook endpoint. (Operator authority)


# **create_webhook_endpoint**
> WebhookEndpointCreated create_webhook_endpoint(create_webhook_endpoint_request)

Register a webhook endpoint. (Operator authority)

Registers an endpoint that receives signed events derived from the audit chain. An endpoint that receives settlement/audit events is OPERATOR-privileged, so this route is gated by the `GL-Operator` credential channel, not the agent bearer token. The `whsec_` signing secret is returned ONCE, on this call; the reads never re-expose it. Default-off: absent a webhook store, this route is a 404. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest
from general_liquidity.models.webhook_endpoint_created import WebhookEndpointCreated
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
    api_instance = general_liquidity.WebhooksApi(api_client)
    create_webhook_endpoint_request = general_liquidity.CreateWebhookEndpointRequest() # CreateWebhookEndpointRequest | 

    try:
        # Register a webhook endpoint. (Operator authority)
        api_response = api_instance.create_webhook_endpoint(create_webhook_endpoint_request)
        print("The response of WebhooksApi->create_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_endpoint_request** | [**CreateWebhookEndpointRequest**](CreateWebhookEndpointRequest.md)|  | 

### Return type

[**WebhookEndpointCreated**](WebhookEndpointCreated.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created endpoint, including its one-time secret. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_endpoint**
> delete_webhook_endpoint(id)

Delete one webhook endpoint. (Operator authority)

### Example

* Api Key Authentication (operatorAuth):

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

# Configure API key authorization: operatorAuth
configuration.api_key['operatorAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['operatorAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with general_liquidity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_liquidity.WebhooksApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one webhook endpoint. (Operator authority)
        api_instance.delete_webhook_endpoint(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_endpoint**
> WebhookEndpoint get_webhook_endpoint(id)

Read one webhook endpoint. (Operator authority)

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.webhook_endpoint import WebhookEndpoint
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
    api_instance = general_liquidity.WebhooksApi(api_client)
    id = 'id_example' # str | 

    try:
        # Read one webhook endpoint. (Operator authority)
        api_response = api_instance.get_webhook_endpoint(id)
        print("The response of WebhooksApi->get_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WebhookEndpoint**](WebhookEndpoint.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint (secret redacted). |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_endpoints**
> ListWebhookEndpoints200Response list_webhook_endpoints()

List webhook endpoints. (Operator authority)

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.list_webhook_endpoints200_response import ListWebhookEndpoints200Response
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
    api_instance = general_liquidity.WebhooksApi(api_client)

    try:
        # List webhook endpoints. (Operator authority)
        api_response = api_instance.list_webhook_endpoints()
        print("The response of WebhooksApi->list_webhook_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhook_endpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListWebhookEndpoints200Response**](ListWebhookEndpoints200Response.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The registered endpoints (secrets redacted). |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_endpoint**
> WebhookEndpoint update_webhook_endpoint(id, update_webhook_endpoint_request)

Update one webhook endpoint. (Operator authority)

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.update_webhook_endpoint_request import UpdateWebhookEndpointRequest
from general_liquidity.models.webhook_endpoint import WebhookEndpoint
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
    api_instance = general_liquidity.WebhooksApi(api_client)
    id = 'id_example' # str | 
    update_webhook_endpoint_request = general_liquidity.UpdateWebhookEndpointRequest() # UpdateWebhookEndpointRequest | 

    try:
        # Update one webhook endpoint. (Operator authority)
        api_response = api_instance.update_webhook_endpoint(id, update_webhook_endpoint_request)
        print("The response of WebhooksApi->update_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_webhook_endpoint_request** | [**UpdateWebhookEndpointRequest**](UpdateWebhookEndpointRequest.md)|  | 

### Return type

[**WebhookEndpoint**](WebhookEndpoint.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated endpoint (secret redacted). |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**404** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

