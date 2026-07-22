# general_liquidity.CommerceApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy**](CommerceApi.md#buy) | **POST** /buy | Drive a merchant checkout to a completed Order. (Beta)
[**quote**](CommerceApi.md#quote) | **POST** /quote | Get a server-authoritative priced cart before buy. (Beta)


# **buy**
> Order buy(idempotency_key, intent)

Drive a merchant checkout to a completed Order. (Beta)

Beta. Drive a merchant checkout (ACP · UCP) to a completed `Order`; calls `pay` for the authorize/settle beats. Documented but not yet stable. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.intent import Intent
from general_liquidity.models.order import Order
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
    api_instance = general_liquidity.CommerceApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Client-generated, server-enforced idempotency key. Required on all mutating operations (`pay`, `buy`) — on a payment path this is a correctness guarantee against double-spend, not a convenience. 
    intent = general_liquidity.Intent() # Intent | 

    try:
        # Drive a merchant checkout to a completed Order. (Beta)
        api_response = api_instance.buy(idempotency_key, intent)
        print("The response of CommerceApi->buy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommerceApi->buy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Client-generated, server-enforced idempotency key. Required on all mutating operations (&#x60;pay&#x60;, &#x60;buy&#x60;) — on a payment path this is a correctness guarantee against double-spend, not a convenience.  | 
 **intent** | [**Intent**](Intent.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The completed order. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | RFC 7807 problem detail. |  -  |
**409** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote**
> Cart quote(quote_request)

Get a server-authoritative priced cart before buy. (Beta)

Beta. Get a server-authoritative priced `Cart` (tax, inventory, fulfillment computed by the merchant) before committing to `buy`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.cart import Cart
from general_liquidity.models.quote_request import QuoteRequest
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
    api_instance = general_liquidity.CommerceApi(api_client)
    quote_request = general_liquidity.QuoteRequest() # QuoteRequest | 

    try:
        # Get a server-authoritative priced cart before buy. (Beta)
        api_response = api_instance.quote(quote_request)
        print("The response of CommerceApi->quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommerceApi->quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)|  | 

### Return type

[**Cart**](Cart.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A server-authoritative priced cart. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

