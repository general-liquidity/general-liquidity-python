# general_liquidity.OperatorApi

All URIs are relative to *https://api.generalliquidity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operator_approve**](OperatorApi.md#operator_approve) | **POST** /operator/approve | Release a parked (confirm-tier) intent to settlement.
[**operator_kill_switch**](OperatorApi.md#operator_kill_switch) | **POST** /operator/kill-switch | Freeze or unfreeze the settle path.
[**operator_refund**](OperatorApi.md#operator_refund) | **POST** /operator/refund | Reverse a settled payment on a reversible rail.
[**operator_reset_circuit_breaker**](OperatorApi.md#operator_reset_circuit_breaker) | **POST** /operator/circuit-breaker/reset | Clear a tripped circuit breaker.


# **operator_approve**
> Receipt operator_approve(operator_approve)

Release a parked (confirm-tier) intent to settlement.

The network half of the parked-intent flow. A caller who received an `approval.pending` problem holds exactly the fields this route needs — the intent id, the matched mandate id, and the challenge that binds an approval to that intent. The kernel's own preconditions are preserved: a hard deny cannot be approved away, and a high-risk, irreversible or large intent that arrives without an explicit `acknowledged` comes back as another `approval.pending` (the settler's challenge-response), never a settlement. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.operator_approve import OperatorApprove
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

# Configure API key authorization: operatorAuth
configuration.api_key['operatorAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['operatorAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with general_liquidity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_liquidity.OperatorApi(api_client)
    operator_approve = general_liquidity.OperatorApprove() # OperatorApprove | 

    try:
        # Release a parked (confirm-tier) intent to settlement.
        api_response = api_instance.operator_approve(operator_approve)
        print("The response of OperatorApi->operator_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorApi->operator_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_approve** | [**OperatorApprove**](OperatorApprove.md)|  | 

### Return type

[**Receipt**](Receipt.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approved and settled. The durable Receipt. |  -  |
**202** | The settler withheld release pending explicit acknowledgement. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**409** | RFC 7807 problem detail. |  -  |
**413** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_kill_switch**
> OperatorStateView operator_kill_switch(operator_kill_switch)

Freeze or unfreeze the settle path.

Engage or disengage the kill switch. While engaged, no payment settles — the agent cannot write this flag, so it is a genuine operator brake for an incident. The two directions are signed separately, so an \"unfreeze\" credential cannot be replayed as a freeze. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.operator_kill_switch import OperatorKillSwitch
from general_liquidity.models.operator_state_view import OperatorStateView
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
    api_instance = general_liquidity.OperatorApi(api_client)
    operator_kill_switch = general_liquidity.OperatorKillSwitch() # OperatorKillSwitch | 

    try:
        # Freeze or unfreeze the settle path.
        api_response = api_instance.operator_kill_switch(operator_kill_switch)
        print("The response of OperatorApi->operator_kill_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorApi->operator_kill_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_kill_switch** | [**OperatorKillSwitch**](OperatorKillSwitch.md)|  | 

### Return type

[**OperatorStateView**](OperatorStateView.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The live halt state after the operation. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**413** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_refund**
> RefundResult operator_refund(operator_refund)

Reverse a settled payment on a reversible rail.

Reverse a settled payment, resolving to the PSP that issued the receipt. Refusing an irreversible refund is a safety property, not a limitation: a settlement on an irreversible rail comes back `operator.refused`. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.operator_refund import OperatorRefund
from general_liquidity.models.refund_result import RefundResult
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
    api_instance = general_liquidity.OperatorApi(api_client)
    operator_refund = general_liquidity.OperatorRefund() # OperatorRefund | 

    try:
        # Reverse a settled payment on a reversible rail.
        api_response = api_instance.operator_refund(operator_refund)
        print("The response of OperatorApi->operator_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorApi->operator_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_refund** | [**OperatorRefund**](OperatorRefund.md)|  | 

### Return type

[**RefundResult**](RefundResult.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The refund result. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**409** | RFC 7807 problem detail. |  -  |
**413** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_reset_circuit_breaker**
> OperatorStateView operator_reset_circuit_breaker(operator_rationale)

Clear a tripped circuit breaker.

Reset the circuit breaker after it trips on consecutive blocks or failures, re-enabling auto-execution. An operator-only control. 

### Example

* Api Key Authentication (operatorAuth):

```python
import general_liquidity
from general_liquidity.models.operator_rationale import OperatorRationale
from general_liquidity.models.operator_state_view import OperatorStateView
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
    api_instance = general_liquidity.OperatorApi(api_client)
    operator_rationale = general_liquidity.OperatorRationale() # OperatorRationale | 

    try:
        # Clear a tripped circuit breaker.
        api_response = api_instance.operator_reset_circuit_breaker(operator_rationale)
        print("The response of OperatorApi->operator_reset_circuit_breaker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatorApi->operator_reset_circuit_breaker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_rationale** | [**OperatorRationale**](OperatorRationale.md)|  | 

### Return type

[**OperatorStateView**](OperatorStateView.md)

### Authorization

[operatorAuth](../README.md#operatorAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The live halt state after the reset. |  -  |
**400** | RFC 7807 problem detail. |  -  |
**401** | RFC 7807 problem detail. |  -  |
**413** | RFC 7807 problem detail. |  -  |
**429** | RFC 7807 problem detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

