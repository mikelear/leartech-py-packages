# webcoder_service.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_me_get**](AuthApi.md#api_v1_me_get) | **GET** /api/v1/me | Return claims for the authenticated caller


# **api_v1_me_get**
> HandlersMeResponse api_v1_me_get()

Return claims for the authenticated caller

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.models.handlers_me_response import HandlersMeResponse
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.AuthApi(api_client)

    try:
        # Return claims for the authenticated caller
        api_response = await api_instance.api_v1_me_get()
        print("The response of AuthApi->api_v1_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->api_v1_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersMeResponse**](HandlersMeResponse.md)

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

