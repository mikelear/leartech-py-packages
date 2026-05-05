# webcoder_service.InitiativesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_initiatives_run_id_delete**](InitiativesApi.md#api_v1_initiatives_run_id_delete) | **DELETE** /api/v1/initiatives/{runId} | Kill a running initiative run
[**api_v1_initiatives_run_id_get**](InitiativesApi.md#api_v1_initiatives_run_id_get) | **GET** /api/v1/initiatives/{runId} | Get a single initiative run by run ID
[**api_v1_initiatives_run_id_logs_get**](InitiativesApi.md#api_v1_initiatives_run_id_logs_get) | **GET** /api/v1/initiatives/{runId}/logs | Stream or fetch logs for an initiative run
[**api_v1_projects_project_id_initiatives_get**](InitiativesApi.md#api_v1_projects_project_id_initiatives_get) | **GET** /api/v1/projects/{projectId}/initiatives | List initiative runs for a project
[**api_v1_projects_project_id_initiatives_post**](InitiativesApi.md#api_v1_projects_project_id_initiatives_post) | **POST** /api/v1/projects/{projectId}/initiatives | Trigger a new initiative run for a project


# **api_v1_initiatives_run_id_delete**
> Dict[str, str] api_v1_initiatives_run_id_delete(run_id)

Kill a running initiative run

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.InitiativesApi(api_client)
    run_id = 'run_id_example' # str | Run ID

    try:
        # Kill a running initiative run
        api_response = await api_instance.api_v1_initiatives_run_id_delete(run_id)
        print("The response of InitiativesApi->api_v1_initiatives_run_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitiativesApi->api_v1_initiatives_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run ID | 

### Return type

**Dict[str, str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_initiatives_run_id_get**
> HandlersInitiativeRun api_v1_initiatives_run_id_get(run_id)

Get a single initiative run by run ID

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.models.handlers_initiative_run import HandlersInitiativeRun
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.InitiativesApi(api_client)
    run_id = 'run_id_example' # str | Run ID

    try:
        # Get a single initiative run by run ID
        api_response = await api_instance.api_v1_initiatives_run_id_get(run_id)
        print("The response of InitiativesApi->api_v1_initiatives_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitiativesApi->api_v1_initiatives_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run ID | 

### Return type

[**HandlersInitiativeRun**](HandlersInitiativeRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_initiatives_run_id_logs_get**
> Dict[str, str] api_v1_initiatives_run_id_logs_get(run_id)

Stream or fetch logs for an initiative run

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.InitiativesApi(api_client)
    run_id = 'run_id_example' # str | Run ID

    try:
        # Stream or fetch logs for an initiative run
        api_response = await api_instance.api_v1_initiatives_run_id_logs_get(run_id)
        print("The response of InitiativesApi->api_v1_initiatives_run_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitiativesApi->api_v1_initiatives_run_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run ID | 

### Return type

**Dict[str, str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_project_id_initiatives_get**
> List[HandlersInitiativeRun] api_v1_projects_project_id_initiatives_get(project_id)

List initiative runs for a project

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.models.handlers_initiative_run import HandlersInitiativeRun
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.InitiativesApi(api_client)
    project_id = 'project_id_example' # str | Project ID

    try:
        # List initiative runs for a project
        api_response = await api_instance.api_v1_projects_project_id_initiatives_get(project_id)
        print("The response of InitiativesApi->api_v1_projects_project_id_initiatives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitiativesApi->api_v1_projects_project_id_initiatives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 

### Return type

[**List[HandlersInitiativeRun]**](HandlersInitiativeRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_project_id_initiatives_post**
> HandlersCreateInitiativeResponse api_v1_projects_project_id_initiatives_post(project_id, body)

Trigger a new initiative run for a project

### Example

* Api Key Authentication (BearerAuth):

```python
import webcoder_service
from webcoder_service.models.handlers_create_initiative_request import HandlersCreateInitiativeRequest
from webcoder_service.models.handlers_create_initiative_response import HandlersCreateInitiativeResponse
from webcoder_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webcoder_service.Configuration(
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
async with webcoder_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webcoder_service.InitiativesApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    body = webcoder_service.HandlersCreateInitiativeRequest() # HandlersCreateInitiativeRequest | Initiative request

    try:
        # Trigger a new initiative run for a project
        api_response = await api_instance.api_v1_projects_project_id_initiatives_post(project_id, body)
        print("The response of InitiativesApi->api_v1_projects_project_id_initiatives_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitiativesApi->api_v1_projects_project_id_initiatives_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **body** | [**HandlersCreateInitiativeRequest**](HandlersCreateInitiativeRequest.md)| Initiative request | 

### Return type

[**HandlersCreateInitiativeResponse**](HandlersCreateInitiativeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

