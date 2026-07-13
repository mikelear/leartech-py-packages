# leartech_ai_gateway.EmbeddingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_embeddings_post**](EmbeddingsApi.md#v1_embeddings_post) | **POST** /v1/embeddings | Embeddings (not yet implemented)


# **v1_embeddings_post**
> v1_embeddings_post()

Embeddings (not yet implemented)

### Example


```python
import leartech_ai_gateway
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

    try:
        # Embeddings (not yet implemented)
        await api_instance.v1_embeddings_post()
    except Exception as e:
        print("Exception when calling EmbeddingsApi->v1_embeddings_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

