# leartech_lighthouse_pr_events.FleetTestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_fleet_test_get**](FleetTestApi.md#api_v1_fleet_test_get) | **GET** /api/v1/fleet-test | Fleet test endpoint — calls peer template SDKs to prove cross-service auth + SDK wiring.


# **api_v1_fleet_test_get**
> HandlersFleetTestResponse api_v1_fleet_test_get()

Fleet test endpoint — calls peer template SDKs to prove cross-service auth + SDK wiring.

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_lighthouse_pr_events
from leartech_lighthouse_pr_events.models.handlers_fleet_test_response import HandlersFleetTestResponse
from leartech_lighthouse_pr_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_lighthouse_pr_events.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_lighthouse_pr_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_lighthouse_pr_events.FleetTestApi(api_client)

    try:
        # Fleet test endpoint — calls peer template SDKs to prove cross-service auth + SDK wiring.
        api_response = await api_instance.api_v1_fleet_test_get()
        print("The response of FleetTestApi->api_v1_fleet_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetTestApi->api_v1_fleet_test_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersFleetTestResponse**](HandlersFleetTestResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

