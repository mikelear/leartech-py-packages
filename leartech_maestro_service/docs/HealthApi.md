# leartech_maestro_service.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](HealthApi.md#health) | **GET** /health | Gets the health of the service


# **health**
> health()

Gets the health of the service

get the health of the dependencies of the service

### Example


```python
import leartech_maestro_service
from leartech_maestro_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_maestro_service.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_maestro_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_maestro_service.HealthApi(api_client)

    try:
        # Gets the health of the service
        await api_instance.health()
    except Exception as e:
        print("Exception when calling HealthApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

