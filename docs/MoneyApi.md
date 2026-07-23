# general_liquidity.MoneyApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay**](MoneyApi.md#pay) | **POST** /pay | Submit a signed Intent; the gate decides and settles.


# **pay**
> Receipt pay(idempotency_key, intent)

Submit a signed Intent; the gate decides and settles.

Submit a signed `Intent`. The sovereign gate evaluates mandate · caps · risk · velocity · deny-list over the six irreducible `Terms`. On `allow` it settles on the routed rail and returns a durable `Receipt`. On `confirm` it returns a human-approval requirement (RFC 7807). On `deny` it refuses. The caller never holds a settle primitive. 

### Example

* Bearer Authentication (bearerAuth):

```python
import general_liquidity
from general_liquidity.models.intent import Intent
from general_liquidity.models.receipt import Receipt
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
    api_instance = general_liquidity.MoneyApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Client-generated, server-enforced idempotency key. Required on all mutating operations (`pay`, `buy`) — on a payment path this is a correctness guarantee against double-spend, not a convenience. 
    intent = general_liquidity.Intent() # Intent | 

    try:
        # Submit a signed Intent; the gate decides and settles.
        api_response = api_instance.pay(idempotency_key, intent)
        print("The response of MoneyApi->pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoneyApi->pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Client-generated, server-enforced idempotency key. Required on all mutating operations (&#x60;pay&#x60;, &#x60;buy&#x60;) — on a payment path this is a correctness guarantee against double-spend, not a convenience.  | 
 **intent** | [**Intent**](Intent.md)|  | 

### Return type

[**Receipt**](Receipt.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settled. A durable, machine-parseable Receipt. |  -  |
**202** | Accepted but not settled. Either the gate returned &#x60;confirm&#x60; (a human-approval &#x60;Decision&#x60; is returned), or — on a deployment that wired the optional clearing band&#39;s PENDING state — the spend is bound to an obligation whose admissibility floor is not yet met and its deadline has not passed, so the value is HELD (&#x60;PendingSettlement&#x60;, problem type &#x60;clearing.pending&#x60;) naming the awaited evidence class. The hold auto-releases on a later attempt once admissible evidence exists, or refuses once the deadline passes. Both are default-off: a stack without a PENDING clearing band never returns &#x60;PendingSettlement&#x60;.  |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**403** | Gate returned &#x60;deny&#x60;. The Intent falls outside mandate/policy. |  -  |
**409** | RFC 7807 problem detail. |  -  |
**422** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

