# leartech_auth_service.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](UserApi.md#get_me) | **GET** /api/auth/me | Get current user info


# **get_me**
> ModelsAuthResponse get_me(user_id)

Get current user info

Returns user profile, permissions, and display name

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.models_auth_response import ModelsAuthResponse
from leartech_auth_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_auth_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_auth_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_auth_service.UserApi(api_client)
    user_id = 'user_id_example' # str | User ID

    try:
        # Get current user info
        api_response = await api_instance.get_me(user_id)
        print("The response of UserApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

### Return type

[**ModelsAuthResponse**](ModelsAuthResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

