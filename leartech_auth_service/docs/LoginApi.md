# leartech_auth_service.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_consent**](LoginApi.md#get_consent) | **GET** /api/auth/consent | Process OAuth2 consent
[**get_login**](LoginApi.md#get_login) | **GET** /api/auth/login | Get login challenge from Hydra
[**get_logout**](LoginApi.md#get_logout) | **GET** /api/auth/logout | Handle Hydra logout callback
[**post_login**](LoginApi.md#post_login) | **POST** /api/auth/login | Submit login credentials


# **get_consent**
> get_consent(consent_challenge)

Process OAuth2 consent

Auto-accepts consent for first-party clients, injecting user permissions into token claims

### Example


```python
import leartech_auth_service
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
    api_instance = leartech_auth_service.LoginApi(api_client)
    consent_challenge = 'consent_challenge_example' # str | Hydra consent challenge

    try:
        # Process OAuth2 consent
        await api_instance.get_consent(consent_challenge)
    except Exception as e:
        print("Exception when calling LoginApi->get_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_challenge** | **str**| Hydra consent challenge | 

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
**302** | Redirect to Hydra with tokens |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login**
> Dict[str, object] get_login(login_challenge)

Get login challenge from Hydra

Checks the login challenge and returns challenge info or redirects if session exists

### Example


```python
import leartech_auth_service
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
    api_instance = leartech_auth_service.LoginApi(api_client)
    login_challenge = 'login_challenge_example' # str | Hydra login challenge

    try:
        # Get login challenge from Hydra
        api_response = await api_instance.get_login(login_challenge)
        print("The response of LoginApi->get_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->get_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_challenge** | **str**| Hydra login challenge | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**302** | Redirect to Hydra |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logout**
> get_logout(logout_challenge)

Handle Hydra logout callback

Accepts the logout challenge to revoke the Hydra session

### Example


```python
import leartech_auth_service
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
    api_instance = leartech_auth_service.LoginApi(api_client)
    logout_challenge = 'logout_challenge_example' # str | Hydra logout challenge

    try:
        # Handle Hydra logout callback
        await api_instance.get_logout(logout_challenge)
    except Exception as e:
        print("Exception when calling LoginApi->get_logout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logout_challenge** | **str**| Hydra logout challenge | 

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
**302** | Redirect to auth-ui |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_login**
> Dict[str, object] post_login(login_challenge, credentials)

Submit login credentials

Validates email/password, checks 2FA requirement, and accepts/rejects the Hydra login

### Example


```python
import leartech_auth_service
from leartech_auth_service.models.login_request import LoginRequest
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
    api_instance = leartech_auth_service.LoginApi(api_client)
    login_challenge = 'login_challenge_example' # str | Hydra login challenge
    credentials = leartech_auth_service.LoginRequest() # LoginRequest | Login credentials

    try:
        # Submit login credentials
        api_response = await api_instance.post_login(login_challenge, credentials)
        print("The response of LoginApi->post_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->post_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_challenge** | **str**| Hydra login challenge | 
 **credentials** | [**LoginRequest**](LoginRequest.md)| Login credentials | 

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

