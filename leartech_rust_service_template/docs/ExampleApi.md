# leartech_rust_service_template.ExampleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example**](ExampleApi.md#example) | **GET** /api/v1/example | Example endpoint — protected by &#x60;AuthLayer&#x60;, returns the caller&#39;s &#x60;user_id&#x60;.


# **example**
> ExampleResponse example()

Example endpoint — protected by `AuthLayer`, returns the caller's `user_id`.

The `Claims` extractor pulls the validated token claims out of request
extensions where `AuthLayer` placed them. If the layer wasn't applied, the
extractor returns 500 (operator misconfig — distinct from a client-side
401/403 the layer itself would have produced for invalid tokens).

### Example


```python
import leartech_rust_service_template
from leartech_rust_service_template.models.example_response import ExampleResponse
from leartech_rust_service_template.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_rust_service_template.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_rust_service_template.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_rust_service_template.ExampleApi(api_client)

    try:
        # Example endpoint — protected by `AuthLayer`, returns the caller's `user_id`.
        api_response = await api_instance.example()
        print("The response of ExampleApi->example:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExampleApi->example: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExampleResponse**](ExampleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validated |  -  |
**401** | Bearer token missing or invalid |  -  |
**403** | Token valid but insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

