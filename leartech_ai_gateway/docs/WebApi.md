# leartech_ai_gateway.WebApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_fetch_post**](WebApi.md#v1_fetch_post) | **POST** /v1/fetch | URL fetch (gated on the web_fetch scope)
[**v1_search_post**](WebApi.md#v1_search_post) | **POST** /v1/search | Web search (gated on the web_search scope)


# **v1_fetch_post**
> WebfetchResult v1_fetch_post()

URL fetch (gated on the web_fetch scope)

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.webfetch_result import WebfetchResult
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
    api_instance = leartech_ai_gateway.WebApi(api_client)

    try:
        # URL fetch (gated on the web_fetch scope)
        api_response = await api_instance.v1_fetch_post()
        print("The response of WebApi->v1_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->v1_fetch_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebfetchResult**](WebfetchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_search_post**
> WebsearchResults v1_search_post()

Web search (gated on the web_search scope)

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.websearch_results import WebsearchResults
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
    api_instance = leartech_ai_gateway.WebApi(api_client)

    try:
        # Web search (gated on the web_search scope)
        api_response = await api_instance.v1_search_post()
        print("The response of WebApi->v1_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebApi->v1_search_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebsearchResults**](WebsearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

