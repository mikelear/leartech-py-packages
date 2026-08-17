# leartech_lighthouse_pr_events.WebhookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lighthouse_events_post**](WebhookApi.md#lighthouse_events_post) | **POST** /lighthouse/events | Lighthouse external-plugin webhook receiver


# **lighthouse_events_post**
> Dict[str, str] lighthouse_events_post()

Lighthouse external-plugin webhook receiver

### Example


```python
import leartech_lighthouse_pr_events
from leartech_lighthouse_pr_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_lighthouse_pr_events.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with leartech_lighthouse_pr_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_lighthouse_pr_events.WebhookApi(api_client)

    try:
        # Lighthouse external-plugin webhook receiver
        api_response = await api_instance.lighthouse_events_post()
        print("The response of WebhookApi->lighthouse_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->lighthouse_events_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

