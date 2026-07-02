# leartech_auth_service.DCRApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_cr_register**](DCRApi.md#d_cr_register) | **POST** /oauth2/register | Dynamic Client Registration (RFC 7591)


# **d_cr_register**
> ModelsDCRRegisterResponse d_cr_register(body)

Dynamic Client Registration (RFC 7591)

Accepts a public client registration request, validates it against the configured policy, forwards to Hydra, and returns the issued client_id/client_secret.

### Example


```python
import leartech_auth_service
from leartech_auth_service.models.models_dcr_register_request import ModelsDCRRegisterRequest
from leartech_auth_service.models.models_dcr_register_response import ModelsDCRRegisterResponse
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
    api_instance = leartech_auth_service.DCRApi(api_client)
    body = leartech_auth_service.ModelsDCRRegisterRequest() # ModelsDCRRegisterRequest | Registration payload

    try:
        # Dynamic Client Registration (RFC 7591)
        api_response = await api_instance.d_cr_register(body)
        print("The response of DCRApi->d_cr_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCRApi->d_cr_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsDCRRegisterRequest**](ModelsDCRRegisterRequest.md)| Registration payload | 

### Return type

[**ModelsDCRRegisterResponse**](ModelsDCRRegisterResponse.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

