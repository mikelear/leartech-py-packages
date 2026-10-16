# leartech_platform_capabilities_api.CapabilitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_capabilities_languages_get**](CapabilitiesApi.md#api_v1_capabilities_languages_get) | **GET** /api/v1/capabilities/languages | List supported languages
[**api_v1_capabilities_languages_name_get**](CapabilitiesApi.md#api_v1_capabilities_languages_name_get) | **GET** /api/v1/capabilities/languages/{name} | Resolve one language
[**api_v1_capabilities_promote_post**](CapabilitiesApi.md#api_v1_capabilities_promote_post) | **POST** /api/v1/capabilities/promote | Promote a researched capability
[**api_v1_capabilities_stores_get**](CapabilitiesApi.md#api_v1_capabilities_stores_get) | **GET** /api/v1/capabilities/stores | List supported stores
[**api_v1_capabilities_stores_name_get**](CapabilitiesApi.md#api_v1_capabilities_stores_name_get) | **GET** /api/v1/capabilities/stores/{name} | Resolve one store


# **api_v1_capabilities_languages_get**
> Dict[str, object] api_v1_capabilities_languages_get()

List supported languages

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_platform_capabilities_api
from leartech_platform_capabilities_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_platform_capabilities_api.Configuration(
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
async with leartech_platform_capabilities_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_platform_capabilities_api.CapabilitiesApi(api_client)

    try:
        # List supported languages
        api_response = await api_instance.api_v1_capabilities_languages_get()
        print("The response of CapabilitiesApi->api_v1_capabilities_languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->api_v1_capabilities_languages_get: %s\n" % e)
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

# **api_v1_capabilities_languages_name_get**
> Dict[str, object] api_v1_capabilities_languages_name_get(name)

Resolve one language

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_platform_capabilities_api
from leartech_platform_capabilities_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_platform_capabilities_api.Configuration(
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
async with leartech_platform_capabilities_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_platform_capabilities_api.CapabilitiesApi(api_client)
    name = 'name_example' # str | capability name to resolve

    try:
        # Resolve one language
        api_response = await api_instance.api_v1_capabilities_languages_name_get(name)
        print("The response of CapabilitiesApi->api_v1_capabilities_languages_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->api_v1_capabilities_languages_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| capability name to resolve | 

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

# **api_v1_capabilities_promote_post**
> CapabilitiesPromoteResult api_v1_capabilities_promote_post()

Promote a researched capability

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_platform_capabilities_api
from leartech_platform_capabilities_api.models.capabilities_promote_result import CapabilitiesPromoteResult
from leartech_platform_capabilities_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_platform_capabilities_api.Configuration(
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
async with leartech_platform_capabilities_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_platform_capabilities_api.CapabilitiesApi(api_client)

    try:
        # Promote a researched capability
        api_response = await api_instance.api_v1_capabilities_promote_post()
        print("The response of CapabilitiesApi->api_v1_capabilities_promote_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->api_v1_capabilities_promote_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CapabilitiesPromoteResult**](CapabilitiesPromoteResult.md)

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

# **api_v1_capabilities_stores_get**
> Dict[str, object] api_v1_capabilities_stores_get()

List supported stores

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_platform_capabilities_api
from leartech_platform_capabilities_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_platform_capabilities_api.Configuration(
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
async with leartech_platform_capabilities_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_platform_capabilities_api.CapabilitiesApi(api_client)

    try:
        # List supported stores
        api_response = await api_instance.api_v1_capabilities_stores_get()
        print("The response of CapabilitiesApi->api_v1_capabilities_stores_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->api_v1_capabilities_stores_get: %s\n" % e)
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

# **api_v1_capabilities_stores_name_get**
> Dict[str, object] api_v1_capabilities_stores_name_get(name)

Resolve one store

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_platform_capabilities_api
from leartech_platform_capabilities_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_platform_capabilities_api.Configuration(
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
async with leartech_platform_capabilities_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_platform_capabilities_api.CapabilitiesApi(api_client)
    name = 'name_example' # str | capability name to resolve

    try:
        # Resolve one store
        api_response = await api_instance.api_v1_capabilities_stores_name_get(name)
        print("The response of CapabilitiesApi->api_v1_capabilities_stores_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->api_v1_capabilities_stores_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| capability name to resolve | 

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

