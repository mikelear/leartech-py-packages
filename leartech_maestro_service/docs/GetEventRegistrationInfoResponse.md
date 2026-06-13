# GetEventRegistrationInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** |  | [optional] 
**event_registrations** | [**List[EventRegistrationInfo]**](EventRegistrationInfo.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.get_event_registration_info_response import GetEventRegistrationInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventRegistrationInfoResponse from a JSON string
get_event_registration_info_response_instance = GetEventRegistrationInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventRegistrationInfoResponse.to_json())

# convert the object into a dict
get_event_registration_info_response_dict = get_event_registration_info_response_instance.to_dict()
# create an instance of GetEventRegistrationInfoResponse from a dict
get_event_registration_info_response_from_dict = GetEventRegistrationInfoResponse.from_dict(get_event_registration_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


