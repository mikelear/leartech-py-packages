# leartech_auth_service.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_activate_user**](AdminApi.md#admin_activate_user) | **POST** /api/auth/admin/users/{id}/activate | Activate a user
[**admin_create_tenant**](AdminApi.md#admin_create_tenant) | **POST** /api/auth/admin/tenants | Create a tenant
[**admin_create_user**](AdminApi.md#admin_create_user) | **POST** /api/auth/admin/users | Create a user (tenant-fenced)
[**admin_deactivate_user**](AdminApi.md#admin_deactivate_user) | **POST** /api/auth/admin/users/{id}/deactivate | Deactivate a user
[**admin_delete_tenant**](AdminApi.md#admin_delete_tenant) | **DELETE** /api/auth/admin/tenants/{id} | Delete a tenant
[**admin_delete_user**](AdminApi.md#admin_delete_user) | **DELETE** /api/auth/admin/users/{id} | Delete a user (tenant-fenced)
[**admin_get_tenant**](AdminApi.md#admin_get_tenant) | **GET** /api/auth/admin/tenants/{id} | Get a tenant by ID
[**admin_get_user**](AdminApi.md#admin_get_user) | **GET** /api/auth/admin/users/{id} | Get a user by ID (tenant-fenced)
[**admin_list_audit**](AdminApi.md#admin_list_audit) | **GET** /api/auth/admin/audit | List the admin audit log for the caller&#39;s tenant
[**admin_list_tenants**](AdminApi.md#admin_list_tenants) | **GET** /api/auth/admin/tenants | List all tenants
[**admin_list_users**](AdminApi.md#admin_list_users) | **GET** /api/auth/admin/users | List users in the caller&#39;s tenant
[**admin_reset_passkeys**](AdminApi.md#admin_reset_passkeys) | **POST** /api/auth/admin/users/{id}/passkeys/reset | Reset a user&#39;s passkeys (tenant-fenced)
[**admin_reset_two_factor**](AdminApi.md#admin_reset_two_factor) | **POST** /api/auth/admin/users/{id}/2fa/reset | Reset a user&#39;s 2FA (tenant-fenced)
[**admin_set_user_permissions**](AdminApi.md#admin_set_user_permissions) | **PUT** /api/auth/admin/users/{id}/permissions | Set a user&#39;s permissions
[**admin_set_user_role**](AdminApi.md#admin_set_user_role) | **PUT** /api/auth/admin/users/{id}/role | Set a user&#39;s role
[**admin_update_user**](AdminApi.md#admin_update_user) | **PUT** /api/auth/admin/users/{id} | Update a user&#39;s profile (tenant-fenced)


# **admin_activate_user**
> User admin_activate_user(id)

Activate a user

Admin-only, tenant-fenced. Re-enables a deactivated account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Activate a user
        api_response = await api_instance.admin_activate_user(id)
        print("The response of AdminApi->admin_activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_tenant**
> Tenant admin_create_tenant(tenant)

Create a tenant

Platform-admin only. Name must be unique (409 otherwise); the id is server-assigned. Audited.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_create_tenant_request import AdminCreateTenantRequest
from leartech_auth_service.models.tenant import Tenant
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    tenant = leartech_auth_service.AdminCreateTenantRequest() # AdminCreateTenantRequest | New tenant

    try:
        # Create a tenant
        api_response = await api_instance.admin_create_tenant(tenant)
        print("The response of AdminApi->admin_create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | [**AdminCreateTenantRequest**](AdminCreateTenantRequest.md)| New tenant | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_user**
> User admin_create_user(user)

Create a user (tenant-fenced)

Admin-only. Creates a user in the caller's tenant. Email must be unique (409). Granting platform-admin role/permission requires a platform admin. Audited.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_create_user_request import AdminCreateUserRequest
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    user = leartech_auth_service.AdminCreateUserRequest() # AdminCreateUserRequest | New user

    try:
        # Create a user (tenant-fenced)
        api_response = await api_instance.admin_create_user(user)
        print("The response of AdminApi->admin_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**AdminCreateUserRequest**](AdminCreateUserRequest.md)| New user | 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_deactivate_user**
> User admin_deactivate_user(id)

Deactivate a user

Admin-only, tenant-fenced. A deactivated user cannot log in. An admin cannot deactivate themselves.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Deactivate a user
        api_response = await api_instance.admin_deactivate_user(id)
        print("The response of AdminApi->admin_deactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_deactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

[**User**](User.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_tenant**
> admin_delete_tenant(id)

Delete a tenant

Platform-admin only. The platform tenant cannot be deleted (409). Audited.

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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | Tenant ID

    try:
        # Delete a tenant
        await api_instance.admin_delete_tenant(id)
    except Exception as e:
        print("Exception when calling AdminApi->admin_delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tenant ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_user**
> admin_delete_user(id)

Delete a user (tenant-fenced)

Admin-only. Hard-deletes a user in the caller's tenant (and their 2FA/passkeys). An admin cannot delete themselves. Audited.

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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Delete a user (tenant-fenced)
        await api_instance.admin_delete_user(id)
    except Exception as e:
        print("Exception when calling AdminApi->admin_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_tenant**
> Tenant admin_get_tenant(id)

Get a tenant by ID

Platform-admin only.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.tenant import Tenant
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | Tenant ID

    try:
        # Get a tenant by ID
        api_response = await api_instance.admin_get_tenant(id)
        print("The response of AdminApi->admin_get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_get_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tenant ID | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_user**
> AdminUserResponse admin_get_user(id)

Get a user by ID (tenant-fenced)

Admin-only. Returns the user (with has2FA/hasPasskey status) if they're in the caller's tenant, else 404.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_user_response import AdminUserResponse
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Get a user by ID (tenant-fenced)
        api_response = await api_instance.admin_get_user(id)
        print("The response of AdminApi->admin_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

[**AdminUserResponse**](AdminUserResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_audit**
> Dict[str, object] admin_list_audit(limit=limit, offset=offset, action=action)

List the admin audit log for the caller's tenant

Admin-only. Returns admin_audit_log entries (newest first), paginated. Optional `action` filter (e.g. delete_user).

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
    api_instance = leartech_auth_service.AdminApi(api_client)
    limit = 56 # int | Page size (default 50, max 200) (optional)
    offset = 56 # int | Offset for pagination (default 0) (optional)
    action = 'action_example' # str | Filter by action (optional)

    try:
        # List the admin audit log for the caller's tenant
        api_response = await api_instance.admin_list_audit(limit=limit, offset=offset, action=action)
        print("The response of AdminApi->admin_list_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_list_audit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Page size (default 50, max 200) | [optional] 
 **offset** | **int**| Offset for pagination (default 0) | [optional] 
 **action** | **str**| Filter by action | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_tenants**
> Dict[str, object] admin_list_tenants()

List all tenants

Platform-admin only. Returns all tenants (not tenant-fenced).

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
    api_instance = leartech_auth_service.AdminApi(api_client)

    try:
        # List all tenants
        api_response = await api_instance.admin_list_tenants()
        print("The response of AdminApi->admin_list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_list_tenants: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_users**
> Dict[str, object] admin_list_users()

List users in the caller's tenant

Admin-only. Returns all users in the authenticated admin's tenant.

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
    api_instance = leartech_auth_service.AdminApi(api_client)

    try:
        # List users in the caller's tenant
        api_response = await api_instance.admin_list_users()
        print("The response of AdminApi->admin_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_reset_passkeys**
> Dict[str, object] admin_reset_passkeys(id)

Reset a user's passkeys (tenant-fenced)

Admin-only. Removes all of the user's WebAuthn credentials so they must re-register. Audited.

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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Reset a user's passkeys (tenant-fenced)
        api_response = await api_instance.admin_reset_passkeys(id)
        print("The response of AdminApi->admin_reset_passkeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_reset_passkeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_reset_two_factor**
> admin_reset_two_factor(id)

Reset a user's 2FA (tenant-fenced)

Admin-only. Removes the user's TOTP enrolment so they must re-enrol. Audited.

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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Reset a user's 2FA (tenant-fenced)
        await api_instance.admin_reset_two_factor(id)
    except Exception as e:
        print("Exception when calling AdminApi->admin_reset_two_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | reset |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_set_user_permissions**
> User admin_set_user_permissions(id, permissions)

Set a user's permissions

Admin-only, tenant-fenced. Replaces the permission set (go-common vocabulary is {User, Admin}). An empty array revokes all. An admin cannot remove their own Admin permission.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_set_permissions_request import AdminSetPermissionsRequest
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID
    permissions = leartech_auth_service.AdminSetPermissionsRequest() # AdminSetPermissionsRequest | New permission set

    try:
        # Set a user's permissions
        api_response = await api_instance.admin_set_user_permissions(id, permissions)
        print("The response of AdminApi->admin_set_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_set_user_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 
 **permissions** | [**AdminSetPermissionsRequest**](AdminSetPermissionsRequest.md)| New permission set | 

### Return type

[**User**](User.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_set_user_role**
> User admin_set_user_role(id, role)

Set a user's role

Admin-only, tenant-fenced. Replaces the coarse RBAC role label (surfaced downstream via ext.user_role). Independent of permissions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_set_role_request import AdminSetRoleRequest
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID
    role = leartech_auth_service.AdminSetRoleRequest() # AdminSetRoleRequest | New role

    try:
        # Set a user's role
        api_response = await api_instance.admin_set_user_role(id, role)
        print("The response of AdminApi->admin_set_user_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_set_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 
 **role** | [**AdminSetRoleRequest**](AdminSetRoleRequest.md)| New role | 

### Return type

[**User**](User.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_user**
> User admin_update_user(id, user)

Update a user's profile (tenant-fenced)

Admin-only. Updates the display name. Email/role/permissions have their own endpoints. Audited.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_auth_service
from leartech_auth_service.models.admin_update_user_request import AdminUpdateUserRequest
from leartech_auth_service.models.user import User
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
    api_instance = leartech_auth_service.AdminApi(api_client)
    id = 'id_example' # str | User ID
    user = leartech_auth_service.AdminUpdateUserRequest() # AdminUpdateUserRequest | Profile fields

    try:
        # Update a user's profile (tenant-fenced)
        api_response = await api_instance.admin_update_user(id, user)
        print("The response of AdminApi->admin_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 
 **user** | [**AdminUpdateUserRequest**](AdminUpdateUserRequest.md)| Profile fields | 

### Return type

[**User**](User.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

