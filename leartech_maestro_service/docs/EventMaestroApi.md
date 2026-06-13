# leartech_maestro_service.EventMaestroApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**announce_event**](EventMaestroApi.md#announce_event) | **POST** /api/event_maestro/announce_event | Announces an event for a case to maestro
[**consume_event**](EventMaestroApi.md#consume_event) | **POST** /api/event_maestro/consume_event | Consumes an event for a case from the maestro
[**get_events_by_annotation**](EventMaestroApi.md#get_events_by_annotation) | **GET** /api/event_maestro/events_by_annotation/{annotation_key}/{annotation_value} | Retrieves events by annotation
[**reprocess_event**](EventMaestroApi.md#reprocess_event) | **PUT** /api/event_maestro/reprocess_event/{event_id} | Reprocesses an event from the maestro events log
[**reprocess_event_for_consumer**](EventMaestroApi.md#reprocess_event_for_consumer) | **PUT** /api/event_maestro/reprocess_event_for_consumer/{event_id}/{consumer_name} | Reprocesses an event for a specific consumer


# **announce_event**
> AnnounceEventResponse announce_event(announce_request)

Announces an event for a case to maestro

Announces an event for a case to maestro

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.announce_event_request import AnnounceEventRequest
from leartech_maestro_service.models.announce_event_response import AnnounceEventResponse
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
    api_instance = leartech_maestro_service.EventMaestroApi(api_client)
    announce_request = leartech_maestro_service.AnnounceEventRequest() # AnnounceEventRequest | Event to announce

    try:
        # Announces an event for a case to maestro
        api_response = await api_instance.announce_event(announce_request)
        print("The response of EventMaestroApi->announce_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventMaestroApi->announce_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announce_request** | [**AnnounceEventRequest**](AnnounceEventRequest.md)| Event to announce | 

### Return type

[**AnnounceEventResponse**](AnnounceEventResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consume_event**
> ConsumeEventResponse consume_event(consume_request)

Consumes an event for a case from the maestro

This is a place-holder for consistent package generation, and as an example of the consume endpoint

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.consume_event_request import ConsumeEventRequest
from leartech_maestro_service.models.consume_event_response import ConsumeEventResponse
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
    api_instance = leartech_maestro_service.EventMaestroApi(api_client)
    consume_request = leartech_maestro_service.ConsumeEventRequest() # ConsumeEventRequest | Event to consume

    try:
        # Consumes an event for a case from the maestro
        api_response = await api_instance.consume_event(consume_request)
        print("The response of EventMaestroApi->consume_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventMaestroApi->consume_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consume_request** | [**ConsumeEventRequest**](ConsumeEventRequest.md)| Event to consume | 

### Return type

[**ConsumeEventResponse**](ConsumeEventResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_annotation**
> GetEventsDtoResponse get_events_by_annotation(annotation_key, annotation_value)

Retrieves events by annotation

Retrieves events by annotation

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.get_events_dto_response import GetEventsDtoResponse
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
    api_instance = leartech_maestro_service.EventMaestroApi(api_client)
    annotation_key = 'annotation_key_example' # str | Annotation Key
    annotation_value = 'annotation_value_example' # str | Annotation Value

    try:
        # Retrieves events by annotation
        api_response = await api_instance.get_events_by_annotation(annotation_key, annotation_value)
        print("The response of EventMaestroApi->get_events_by_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventMaestroApi->get_events_by_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_key** | **str**| Annotation Key | 
 **annotation_value** | **str**| Annotation Value | 

### Return type

[**GetEventsDtoResponse**](GetEventsDtoResponse.md)

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

# **reprocess_event**
> Response reprocess_event(event_id, only_failures=only_failures)

Reprocesses an event from the maestro events log

Reprocesses an event from the maestro events log, usually for failed events

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.response import Response
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
    api_instance = leartech_maestro_service.EventMaestroApi(api_client)
    event_id = 'event_id_example' # str | Event ID
    only_failures = True # bool | Only failures (optional)

    try:
        # Reprocesses an event from the maestro events log
        api_response = await api_instance.reprocess_event(event_id, only_failures=only_failures)
        print("The response of EventMaestroApi->reprocess_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventMaestroApi->reprocess_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Event ID | 
 **only_failures** | **bool**| Only failures | [optional] 

### Return type

[**Response**](Response.md)

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

# **reprocess_event_for_consumer**
> Response reprocess_event_for_consumer(event_id, consumer_name)

Reprocesses an event for a specific consumer

Reprocesses an event for a specific consumer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.response import Response
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
    api_instance = leartech_maestro_service.EventMaestroApi(api_client)
    event_id = 'event_id_example' # str | Event ID
    consumer_name = 'consumer_name_example' # str | Consumer Name

    try:
        # Reprocesses an event for a specific consumer
        api_response = await api_instance.reprocess_event_for_consumer(event_id, consumer_name)
        print("The response of EventMaestroApi->reprocess_event_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventMaestroApi->reprocess_event_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Event ID | 
 **consumer_name** | **str**| Consumer Name | 

### Return type

[**Response**](Response.md)

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

