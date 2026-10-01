# leartech_ai_gateway.EmbeddingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_embeddings_post**](EmbeddingsApi.md#v1_embeddings_post) | **POST** /v1/embeddings | Embeddings (OpenAI-shaped)


# **v1_embeddings_post**
> ApiEmbeddingsResponse v1_embeddings_post(request)

Embeddings (OpenAI-shaped)

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_embeddings_response import ApiEmbeddingsResponse
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
    api_instance = leartech_ai_gateway.EmbeddingsApi(api_client)
    request = None # object | embeddings request

    try:
        # Embeddings (OpenAI-shaped)
        api_response = await api_instance.v1_embeddings_post(request)
        print("The response of EmbeddingsApi->v1_embeddings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->v1_embeddings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| embeddings request | 

### Return type

[**ApiEmbeddingsResponse**](ApiEmbeddingsResponse.md)

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

