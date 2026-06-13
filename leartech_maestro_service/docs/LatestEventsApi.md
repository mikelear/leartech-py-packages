# leartech_maestro_service.LatestEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_event_details**](LatestEventsApi.md#get_latest_event_details) | **GET** /api/latest_events/latest_event_details | Retrieves the latest event details for each event


# **get_latest_event_details**
> GetLatestEventsDetailsResponse get_latest_event_details()

Retrieves the latest event details for each event

Retrieves the latest event details for each event

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import leartech_maestro_service
from leartech_maestro_service.models.get_latest_events_details_response import GetLatestEventsDetailsResponse
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
    api_instance = leartech_maestro_service.LatestEventsApi(api_client)

    try:
        # Retrieves the latest event details for each event
        api_response = await api_instance.get_latest_event_details()
        print("The response of LatestEventsApi->get_latest_event_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LatestEventsApi->get_latest_event_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetLatestEventsDetailsResponse**](GetLatestEventsDetailsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

