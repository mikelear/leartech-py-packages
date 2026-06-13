# leartech_maestro_service.EventRegistrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_registration_information**](EventRegistrationApi.md#get_event_registration_information) | **GET** /api/event_registration/event_info | Returns information about event registrations
[**get_event_registration_information_for_name**](EventRegistrationApi.md#get_event_registration_information_for_name) | **GET** /api/event_registration/event_info/{eventName} | Returns information about a given event registrations


# **get_event_registration_information**
> GetEventRegistrationInfoResponse get_event_registration_information()

Returns information about event registrations

Returns information about event registrations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.get_event_registration_info_response import GetEventRegistrationInfoResponse
from leartech_maestro_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_maestro_service.Configuration(
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
async with leartech_maestro_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_maestro_service.EventRegistrationApi(api_client)

    try:
        # Returns information about event registrations
        api_response = await api_instance.get_event_registration_information()
        print("The response of EventRegistrationApi->get_event_registration_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventRegistrationApi->get_event_registration_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetEventRegistrationInfoResponse**](GetEventRegistrationInfoResponse.md)

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

# **get_event_registration_information_for_name**
> GetEventRegistrationInfoForNameResponse get_event_registration_information_for_name(event_name)

Returns information about a given event registrations

Returns information about a given event registrations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.get_event_registration_info_for_name_response import GetEventRegistrationInfoForNameResponse
from leartech_maestro_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_maestro_service.Configuration(
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
async with leartech_maestro_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_maestro_service.EventRegistrationApi(api_client)
    event_name = 'event_name_example' # str | the name of the event to get information for

    try:
        # Returns information about a given event registrations
        api_response = await api_instance.get_event_registration_information_for_name(event_name)
        print("The response of EventRegistrationApi->get_event_registration_information_for_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventRegistrationApi->get_event_registration_information_for_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| the name of the event to get information for | 

### Return type

[**GetEventRegistrationInfoForNameResponse**](GetEventRegistrationInfoForNameResponse.md)

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

