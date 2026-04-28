# leartech_auth_service.TwoFactorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_two_factor**](TwoFactorApi.md#disable_two_factor) | **POST** /api/auth/twofactor/disable | Disable 2FA
[**enable_two_factor**](TwoFactorApi.md#enable_two_factor) | **POST** /api/auth/twofactor/enable | Start 2FA setup
[**submit_two_factor**](TwoFactorApi.md#submit_two_factor) | **POST** /api/auth/twofactor/submit | Submit 2FA code during login
[**verify_two_factor**](TwoFactorApi.md#verify_two_factor) | **POST** /api/auth/twofactor/verify | Verify 2FA setup


# **disable_two_factor**
> Dict[str, object] disable_two_factor(user_id)

Disable 2FA

Removes two-factor authentication for a user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_auth_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_auth_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_auth_service.TwoFactorApi(api_client)
    user_id = 'user_id_example' # str | User ID

    try:
        # Disable 2FA
        api_response = await api_instance.disable_two_factor(user_id)
        print("The response of TwoFactorApi->disable_two_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorApi->disable_two_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_two_factor**
> ModelsTwoFactorEnableResponse enable_two_factor(user_id)

Start 2FA setup

Generates TOTP secret (QR code URL) and recovery codes for a user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.models_two_factor_enable_response import ModelsTwoFactorEnableResponse
from leartech_auth_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_auth_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_auth_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_auth_service.TwoFactorApi(api_client)
    user_id = 'user_id_example' # str | User ID

    try:
        # Start 2FA setup
        api_response = await api_instance.enable_two_factor(user_id)
        print("The response of TwoFactorApi->enable_two_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorApi->enable_two_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 

### Return type

[**ModelsTwoFactorEnableResponse**](ModelsTwoFactorEnableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_two_factor**
> Dict[str, object] submit_two_factor(login_challenge, user_id, code)

Submit 2FA code during login

Validates TOTP code or recovery code to complete authentication

### Example


```python
import leartech_auth_service
from leartech_auth_service.models.models_two_factor_submit_request import ModelsTwoFactorSubmitRequest
from leartech_auth_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_auth_service.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_auth_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_auth_service.TwoFactorApi(api_client)
    login_challenge = 'login_challenge_example' # str | Hydra login challenge
    user_id = 'user_id_example' # str | User ID
    code = leartech_auth_service.ModelsTwoFactorSubmitRequest() # ModelsTwoFactorSubmitRequest | TOTP or recovery code

    try:
        # Submit 2FA code during login
        api_response = await api_instance.submit_two_factor(login_challenge, user_id, code)
        print("The response of TwoFactorApi->submit_two_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorApi->submit_two_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_challenge** | **str**| Hydra login challenge | 
 **user_id** | **str**| User ID | 
 **code** | [**ModelsTwoFactorSubmitRequest**](ModelsTwoFactorSubmitRequest.md)| TOTP or recovery code | 

### Return type

**Dict[str, object]**

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
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_two_factor**
> Dict[str, object] verify_two_factor(user_id, code)

Verify 2FA setup

Validates the first TOTP code to confirm authenticator app is configured correctly

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.models_two_factor_submit_request import ModelsTwoFactorSubmitRequest
from leartech_auth_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_auth_service.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_auth_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_auth_service.TwoFactorApi(api_client)
    user_id = 'user_id_example' # str | User ID
    code = leartech_auth_service.ModelsTwoFactorSubmitRequest() # ModelsTwoFactorSubmitRequest | TOTP code from authenticator

    try:
        # Verify 2FA setup
        api_response = await api_instance.verify_two_factor(user_id, code)
        print("The response of TwoFactorApi->verify_two_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TwoFactorApi->verify_two_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **code** | [**ModelsTwoFactorSubmitRequest**](ModelsTwoFactorSubmitRequest.md)| TOTP code from authenticator | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

