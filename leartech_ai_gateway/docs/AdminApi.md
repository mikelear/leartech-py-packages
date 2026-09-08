# leartech_ai_gateway.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_v1_keys_get**](AdminApi.md#admin_v1_keys_get) | **GET** /admin/v1/keys | List virtual keys for the caller&#39;s tenant
[**admin_v1_keys_keyid_delete**](AdminApi.md#admin_v1_keys_keyid_delete) | **DELETE** /admin/v1/keys/{keyid} | Revoke a virtual key (soft; never deleted)
[**admin_v1_keys_keyid_rotate_post**](AdminApi.md#admin_v1_keys_keyid_rotate_post) | **POST** /admin/v1/keys/{keyid}/rotate | Rotate a key&#39;s secret (returned once)
[**admin_v1_keys_post**](AdminApi.md#admin_v1_keys_post) | **POST** /admin/v1/keys | Mint a virtual key (secret returned once)
[**admin_v1_usage_get**](AdminApi.md#admin_v1_usage_get) | **GET** /admin/v1/usage | Usage and spend for the caller&#39;s tenant this month


# **admin_v1_keys_get**
> ApiListKeysResponse admin_v1_keys_get()

List virtual keys for the caller's tenant

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_list_keys_response import ApiListKeysResponse
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
    api_instance = leartech_ai_gateway.AdminApi(api_client)

    try:
        # List virtual keys for the caller's tenant
        api_response = await api_instance.admin_v1_keys_get()
        print("The response of AdminApi->admin_v1_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_v1_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiListKeysResponse**](ApiListKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_v1_keys_keyid_delete**
> admin_v1_keys_keyid_delete(keyid)

Revoke a virtual key (soft; never deleted)

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
    api_instance = leartech_ai_gateway.AdminApi(api_client)
    keyid = 'keyid_example' # str | key id

    try:
        # Revoke a virtual key (soft; never deleted)
        await api_instance.admin_v1_keys_keyid_delete(keyid)
    except Exception as e:
        print("Exception when calling AdminApi->admin_v1_keys_keyid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyid** | **str**| key id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_v1_keys_keyid_rotate_post**
> ApiCreateKeyResponse admin_v1_keys_keyid_rotate_post(keyid)

Rotate a key's secret (returned once)

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_create_key_response import ApiCreateKeyResponse
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
    api_instance = leartech_ai_gateway.AdminApi(api_client)
    keyid = 'keyid_example' # str | key id

    try:
        # Rotate a key's secret (returned once)
        api_response = await api_instance.admin_v1_keys_keyid_rotate_post(keyid)
        print("The response of AdminApi->admin_v1_keys_keyid_rotate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_v1_keys_keyid_rotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyid** | **str**| key id | 

### Return type

[**ApiCreateKeyResponse**](ApiCreateKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_v1_keys_post**
> ApiCreateKeyResponse admin_v1_keys_post(request)

Mint a virtual key (secret returned once)

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_create_key_request import ApiCreateKeyRequest
from leartech_ai_gateway.models.api_create_key_response import ApiCreateKeyResponse
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
    api_instance = leartech_ai_gateway.AdminApi(api_client)
    request = leartech_ai_gateway.ApiCreateKeyRequest() # ApiCreateKeyRequest | key policy

    try:
        # Mint a virtual key (secret returned once)
        api_response = await api_instance.admin_v1_keys_post(request)
        print("The response of AdminApi->admin_v1_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_v1_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiCreateKeyRequest**](ApiCreateKeyRequest.md)| key policy | 

### Return type

[**ApiCreateKeyResponse**](ApiCreateKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_v1_usage_get**
> ApiUsageResponse admin_v1_usage_get()

Usage and spend for the caller's tenant this month

### Example


```python
import leartech_ai_gateway
from leartech_ai_gateway.models.api_usage_response import ApiUsageResponse
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
    api_instance = leartech_ai_gateway.AdminApi(api_client)

    try:
        # Usage and spend for the caller's tenant this month
        api_response = await api_instance.admin_v1_usage_get()
        print("The response of AdminApi->admin_v1_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_v1_usage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiUsageResponse**](ApiUsageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

