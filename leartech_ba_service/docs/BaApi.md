# leartech_ba_service.BaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_ba_last_get**](BaApi.md#api_v1_ba_last_get) | **GET** /api/v1/ba/last | The last BA pass
[**api_v1_ba_tick_post**](BaApi.md#api_v1_ba_tick_post) | **POST** /api/v1/ba/tick | Run one BA loop pass


# **api_v1_ba_last_get**
> HandlersBAPass api_v1_ba_last_get()

The last BA pass

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_ba_service
from leartech_ba_service.models.handlers_ba_pass import HandlersBAPass
from leartech_ba_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ba_service.Configuration(
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
async with leartech_ba_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ba_service.BaApi(api_client)

    try:
        # The last BA pass
        api_response = await api_instance.api_v1_ba_last_get()
        print("The response of BaApi->api_v1_ba_last_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaApi->api_v1_ba_last_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersBAPass**](HandlersBAPass.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_ba_tick_post**
> HandlersBAPass api_v1_ba_tick_post()

Run one BA loop pass

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_ba_service
from leartech_ba_service.models.handlers_ba_pass import HandlersBAPass
from leartech_ba_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ba_service.Configuration(
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
async with leartech_ba_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ba_service.BaApi(api_client)

    try:
        # Run one BA loop pass
        api_response = await api_instance.api_v1_ba_tick_post()
        print("The response of BaApi->api_v1_ba_tick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaApi->api_v1_ba_tick_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersBAPass**](HandlersBAPass.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

