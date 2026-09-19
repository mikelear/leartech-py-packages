# leartech_ai_gateway.ToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_tools_get**](ToolsApi.md#v1_tools_get) | **GET** /v1/tools | List gateway-hosted tools for this credential


# **v1_tools_get**
> ApiToolsResponse v1_tools_get()

List gateway-hosted tools for this credential

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_tools_response import ApiToolsResponse
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
    api_instance = leartech_ai_gateway.ToolsApi(api_client)

    try:
        # List gateway-hosted tools for this credential
        api_response = await api_instance.v1_tools_get()
        print("The response of ToolsApi->v1_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->v1_tools_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiToolsResponse**](ApiToolsResponse.md)

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

