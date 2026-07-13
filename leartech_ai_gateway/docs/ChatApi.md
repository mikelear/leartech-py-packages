# leartech_ai_gateway.ChatApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_chat_completions_post**](ChatApi.md#v1_chat_completions_post) | **POST** /v1/chat/completions | OpenAI-compatible chat completion


# **v1_chat_completions_post**
> ApiChatCompletionResponse v1_chat_completions_post(request)

OpenAI-compatible chat completion

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_chat_completion_request import ApiChatCompletionRequest
from leartech_ai_gateway.models.api_chat_completion_response import ApiChatCompletionResponse
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
    api_instance = leartech_ai_gateway.ChatApi(api_client)
    request = leartech_ai_gateway.ApiChatCompletionRequest() # ApiChatCompletionRequest | chat request

    try:
        # OpenAI-compatible chat completion
        api_response = await api_instance.v1_chat_completions_post(request)
        print("The response of ChatApi->v1_chat_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->v1_chat_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiChatCompletionRequest**](ApiChatCompletionRequest.md)| chat request | 

### Return type

[**ApiChatCompletionResponse**](ApiChatCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

