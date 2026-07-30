# general_liquidity.CommerceApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy**](CommerceApi.md#buy) | **POST** /buy | Drive a merchant checkout to a completed Order.
[**quote**](CommerceApi.md#quote) | **POST** /quote | Price a cart against a merchant. Commits nothing.


# **buy**
> Order buy(buy_request)

Drive a merchant checkout to a completed Order.

Drive a merchant checkout to `ready`, authorize it through the SAME gate `/pay` uses, and return the completed `Order` carrying the settlement `Receipt`. The merchant stays merchant-of-record. The PRICE is never taken from the caller: it comes from the server-authoritative `Cart` the merchant priced, so this body carries lines, not amounts. The caller holds no settle primitive here either — the engine behind this route is built over the gateway's own gated `pay` and cannot reach a rail any other way.  OPT-IN, DEFAULT-OFF. Served only where the deployment enabled the commerce tier (`StackConfig.commerce: true`); a deployment that did not answers `404 not_found` on this path exactly as if it never existed.  Because it settles, it is under the same fail-closed rule as `/pay`: where the route exists and no authentication is configured, it refuses rather than settling. Replay is server-side and keyed on the body's `idempotencyKey`, namespaced separately from `/pay`'s. A `503 rail.unavailable` is retryable by construction and is the one outcome NOT stored, so the identical request may be re-sent under the same key. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.buy_request import BuyRequest
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
    buy_request = general_liquidity.BuyRequest() # BuyRequest | 

    try:
        # Drive a merchant checkout to a completed Order.
        api_response = api_instance.buy(buy_request)
        print("The response of CommerceApi->buy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommerceApi->buy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_request** | [**BuyRequest**](BuyRequest.md)|  | 

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
**200** | The completed order, carrying the settlement Receipt. |  -  |
**400** | &#x60;never-retry&#x60;. The body failed the boundary check (&#x60;intent.malformed&#x60;: the quote fields above, plus an absent &#x60;idempotencyKey&#x60;, &#x60;purpose&#x60;, &#x60;terms&#x60;, &#x60;envelope.signature&#x60; or &#x60;envelope.mandateId&#x60;), the bytes were not JSON (&#x60;intent.unparseable&#x60;), or the checkout could not be driven to a state that can be authorized (&#x60;intent.malformed&#x60;, with &#x60;reasons&#x60; carrying the cart &#x60;status&#x60;, any &#x60;continueUrl&#x60; and the merchant&#39;s messages).  |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | &#x60;escalate-to-human&#x60;. The gate refused the authorize beat (&#x60;intent.denied&#x60;), byte-identical to what &#x60;/pay&#x60; returns for the same decision. A gate &#x60;confirm&#x60; lands here too: a merchant session cannot be held open across an out-of-band operator approval, so there is no parked intent for &#x60;/operator/approve&#x60; to release. The other source is a merchant refusal the checkout protocol itself classified &#x60;escalate-to-human&#x60;.  |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |
**500** | RFC 7807 problem detail. |  -  |
**503** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote**
> Cart quote(quote_request)

Price a cart against a merchant. Commits nothing.

Get a server-authoritative priced `Cart` — the merchant computes tax, inventory and fulfillment — before committing to `buy`. Moves no money and holds no value, so it is an ordinary agent read on the bearer credential.  OPT-IN, DEFAULT-OFF. Served only where the deployment enabled the commerce tier (`StackConfig.commerce: true`); a deployment that did not answers `404 not_found` on this path exactly as if it never existed. Enabling it is a deployment decision because it opens an outbound HTTP path to arbitrary merchants. 

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
        # Price a cart against a merchant. Commits nothing.
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
**200** | The server-authoritative priced cart. |  -  |
**400** | &#x60;never-retry&#x60;. The body failed the boundary check (&#x60;intent.malformed&#x60;: unknown &#x60;rail&#x60;, absent &#x60;merchant&#x60; / &#x60;currency&#x60;, empty &#x60;lines&#x60;, a line without a non-empty &#x60;id&#x60; or a positive integer &#x60;quantity&#x60;), the bytes were not JSON (&#x60;intent.unparseable&#x60;), or the merchant could not be driven to a priceable state (&#x60;intent.malformed&#x60;, with &#x60;reasons&#x60; carrying the cart &#x60;status&#x60;, any &#x60;continueUrl&#x60; and the merchant&#39;s own messages). A cart stopped at &#x60;escalation_required&#x60; needs a human at that URL; an identical retry cannot terminate.  |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | &#x60;escalate-to-human&#x60;. The checkout protocol classified its own refusal &#x60;escalate-to-human&#x60; (&#x60;intent.denied&#x60;). Rebuilding the request does not change the merchant&#39;s decision.  |  -  |
**404** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |
**503** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

