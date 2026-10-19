# leartech_ai_gateway.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_sessions_transform_post**](SessionsApi.md#v1_sessions_transform_post) | **POST** /v1/sessions/transform | Rewrite a saved session to resume it on a different model


# **v1_sessions_transform_post**
> ApiTransformSessionResponse v1_sessions_transform_post(request)

Rewrite a saved session to resume it on a different model

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_transform_session_request import ApiTransformSessionRequest
from leartech_ai_gateway.models.api_transform_session_response import ApiTransformSessionResponse
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
    api_instance = leartech_ai_gateway.SessionsApi(api_client)
    request = leartech_ai_gateway.ApiTransformSessionRequest() # ApiTransformSessionRequest | the session and the target model

    try:
        # Rewrite a saved session to resume it on a different model
        api_response = await api_instance.v1_sessions_transform_post(request)
        print("The response of SessionsApi->v1_sessions_transform_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->v1_sessions_transform_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiTransformSessionRequest**](ApiTransformSessionRequest.md)| the session and the target model | 

### Return type

[**ApiTransformSessionResponse**](ApiTransformSessionResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

