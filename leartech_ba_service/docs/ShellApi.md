# leartech_ba_service.ShellApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_shell_prompt_get**](ShellApi.md#api_v1_shell_prompt_get) | **GET** /api/v1/shell/prompt | The system prompt for the terminal client


# **api_v1_shell_prompt_get**
> HandlersShellPrompt api_v1_shell_prompt_get()

The system prompt for the terminal client

Served from configuration so a prompt change is a config change rather than a release. The revision is a content hash: it identifies the exact text, so a recorded session can be tied to the guidance that produced it.

### Example


```python
import leartech_ba_service
from leartech_ba_service.models.handlers_shell_prompt import HandlersShellPrompt
from leartech_ba_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ba_service.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_ba_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ba_service.ShellApi(api_client)

    try:
        # The system prompt for the terminal client
        api_response = await api_instance.api_v1_shell_prompt_get()
        print("The response of ShellApi->api_v1_shell_prompt_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShellApi->api_v1_shell_prompt_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersShellPrompt**](HandlersShellPrompt.md)

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

