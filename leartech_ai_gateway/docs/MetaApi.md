# leartech_ai_gateway.MetaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get**](MetaApi.md#version_get) | **GET** /version | Gateway version and wire-contract level


# **version_get**
> ApiVersionResponse version_get()

Gateway version and wire-contract level

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_version_response import ApiVersionResponse
from leartech_ai_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ai_gateway.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_ai_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ai_gateway.MetaApi(api_client)

    try:
        # Gateway version and wire-contract level
        api_response = await api_instance.version_get()
        print("The response of MetaApi->version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiVersionResponse**](ApiVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

