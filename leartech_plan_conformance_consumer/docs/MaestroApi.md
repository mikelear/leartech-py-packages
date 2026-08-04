# leartech_plan_conformance_consumer.MaestroApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirmed_get**](MaestroApi.md#confirmed_get) | **GET** /confirmed | Check whether an event has been consumed
[**consume_event_post**](MaestroApi.md#consume_event_post) | **POST** /consume_event | Maestro event consumer endpoint
[**events_get**](MaestroApi.md#events_get) | **GET** /events | Debug dump of all recorded events


# **confirmed_get**
> Dict[str, object] confirmed_get(name)

Check whether an event has been consumed

### Example


```python
import leartech_plan_conformance_consumer
from leartech_plan_conformance_consumer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_plan_conformance_consumer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_plan_conformance_consumer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_plan_conformance_consumer.MaestroApi(api_client)
    name = 'name_example' # str | Event name to check for (e.g. test.release.deploy_failed)

    try:
        # Check whether an event has been consumed
        api_response = await api_instance.confirmed_get(name)
        print("The response of MaestroApi->confirmed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaestroApi->confirmed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Event name to check for (e.g. test.release.deploy_failed) | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consume_event_post**
> MaestroConsumeEventResponse consume_event_post(body)

Maestro event consumer endpoint

Accept a Maestro ConsumeEventRequest body, record it,
log a single structured JSON line, return the standard
ConsumeEventResponse. Malformed body → 400 + isErrored.

### Example


```python
import leartech_plan_conformance_consumer
from leartech_plan_conformance_consumer.models.maestro_consume_event_request_dto import MaestroConsumeEventRequestDto
from leartech_plan_conformance_consumer.models.maestro_consume_event_response import MaestroConsumeEventResponse
from leartech_plan_conformance_consumer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_plan_conformance_consumer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_plan_conformance_consumer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_plan_conformance_consumer.MaestroApi(api_client)
    body = leartech_plan_conformance_consumer.MaestroConsumeEventRequestDto() # MaestroConsumeEventRequestDto | The event Maestro is delivering

    try:
        # Maestro event consumer endpoint
        api_response = await api_instance.consume_event_post(body)
        print("The response of MaestroApi->consume_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaestroApi->consume_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaestroConsumeEventRequestDto**](MaestroConsumeEventRequestDto.md)| The event Maestro is delivering | 

### Return type

[**MaestroConsumeEventResponse**](MaestroConsumeEventResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get**
> Dict[str, object] events_get()

Debug dump of all recorded events

### Example


```python
import leartech_plan_conformance_consumer
from leartech_plan_conformance_consumer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_plan_conformance_consumer.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_plan_conformance_consumer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_plan_conformance_consumer.MaestroApi(api_client)

    try:
        # Debug dump of all recorded events
        api_response = await api_instance.events_get()
        print("The response of MaestroApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaestroApi->events_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

