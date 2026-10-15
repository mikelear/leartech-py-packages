# leartech_third_party_api.ProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_third_parties_get**](ProvidersApi.md#api_v1_third_parties_get) | **GET** /api/v1/third-parties | List known third-party providers
[**api_v1_third_parties_name_get**](ProvidersApi.md#api_v1_third_parties_name_get) | **GET** /api/v1/third-parties/{name} | Resolve one provider
[**api_v1_third_parties_promote_post**](ProvidersApi.md#api_v1_third_parties_promote_post) | **POST** /api/v1/third-parties/promote | Promote a researched finding


# **api_v1_third_parties_get**
> Dict[str, object] api_v1_third_parties_get()

List known third-party providers

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_third_party_api
from leartech_third_party_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_third_party_api.Configuration(
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
async with leartech_third_party_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_third_party_api.ProvidersApi(api_client)

    try:
        # List known third-party providers
        api_response = await api_instance.api_v1_third_parties_get()
        print("The response of ProvidersApi->api_v1_third_parties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->api_v1_third_parties_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_third_parties_name_get**
> Dict[str, object] api_v1_third_parties_name_get(name)

Resolve one provider

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_third_party_api
from leartech_third_party_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_third_party_api.Configuration(
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
async with leartech_third_party_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_third_party_api.ProvidersApi(api_client)
    name = 'name_example' # str | provider name to resolve

    try:
        # Resolve one provider
        api_response = await api_instance.api_v1_third_parties_name_get(name)
        print("The response of ProvidersApi->api_v1_third_parties_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->api_v1_third_parties_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| provider name to resolve | 

### Return type

**Dict[str, object]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_third_parties_promote_post**
> ProvidersPromoteResult api_v1_third_parties_promote_post()

Promote a researched finding

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_third_party_api
from leartech_third_party_api.models.providers_promote_result import ProvidersPromoteResult
from leartech_third_party_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_third_party_api.Configuration(
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
async with leartech_third_party_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_third_party_api.ProvidersApi(api_client)

    try:
        # Promote a researched finding
        api_response = await api_instance.api_v1_third_parties_promote_post()
        print("The response of ProvidersApi->api_v1_third_parties_promote_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->api_v1_third_parties_promote_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProvidersPromoteResult**](ProvidersPromoteResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

