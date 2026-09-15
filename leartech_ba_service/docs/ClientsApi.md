# leartech_ba_service.ClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_get**](ClientsApi.md#clients_get) | **GET** /clients | List the terminal clients this build carries
[**clients_name_get**](ClientsApi.md#clients_name_get) | **GET** /clients/{name} | Download one terminal client


# **clients_get**
> HandlersClientsResponse clients_get()

List the terminal clients this build carries

Cross-compiled leartech clients, built from the same commit as this service. The response reports the version served and a SHA256 for each binary.

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_ba_service
from leartech_ba_service.models.handlers_clients_response import HandlersClientsResponse
from leartech_ba_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ba_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_ba_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ba_service.ClientsApi(api_client)

    try:
        # List the terminal clients this build carries
        api_response = await api_instance.clients_get()
        print("The response of ClientsApi->clients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->clients_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HandlersClientsResponse**](HandlersClientsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | no or invalid bearer token |  -  |
**501** | this build carries no clients |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_name_get**
> bytearray clients_name_get(name)

Download one terminal client

Serves the named binary. The name is matched against the directory listing, so only what exists can be requested. X-Leartech-Version reports the build.

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_ba_service
from leartech_ba_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_ba_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_ba_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_ba_service.ClientsApi(api_client)
    name = 'name_example' # str | client filename, e.g. leartech-darwin-arm64

    try:
        # Download one terminal client
        api_response = await api_instance.clients_name_get(name)
        print("The response of ClientsApi->clients_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->clients_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| client filename, e.g. leartech-darwin-arm64 | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | no or invalid bearer token |  -  |
**404** | no such client in this build |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

