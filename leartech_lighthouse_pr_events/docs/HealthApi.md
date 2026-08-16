# leartech_lighthouse_pr_events.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_live_get**](HealthApi.md#health_live_get) | **GET** /health/live | Liveness probe
[**health_ready_get**](HealthApi.md#health_ready_get) | **GET** /health/ready | Readiness probe


# **health_live_get**
> Dict[str, str] health_live_get()

Liveness probe

### Example


```python
import leartech_lighthouse_pr_events
from leartech_lighthouse_pr_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_lighthouse_pr_events.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_lighthouse_pr_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_lighthouse_pr_events.HealthApi(api_client)

    try:
        # Liveness probe
        api_response = await api_instance.health_live_get()
        print("The response of HealthApi->health_live_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_live_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_ready_get**
> Dict[str, str] health_ready_get()

Readiness probe

### Example


```python
import leartech_lighthouse_pr_events
from leartech_lighthouse_pr_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_lighthouse_pr_events.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_lighthouse_pr_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_lighthouse_pr_events.HealthApi(api_client)

    try:
        # Readiness probe
        api_response = await api_instance.health_ready_get()
        print("The response of HealthApi->health_ready_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_ready_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

