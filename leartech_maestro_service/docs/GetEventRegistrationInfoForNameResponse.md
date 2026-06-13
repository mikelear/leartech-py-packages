# GetEventRegistrationInfoForNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** |  | [optional] 
**event_registration** | [**EventRegistrationInfo**](EventRegistrationInfo.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.get_event_registration_info_for_name_response import GetEventRegistrationInfoForNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventRegistrationInfoForNameResponse from a JSON string
get_event_registration_info_for_name_response_instance = GetEventRegistrationInfoForNameResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventRegistrationInfoForNameResponse.to_json())

# convert the object into a dict
get_event_registration_info_for_name_response_dict = get_event_registration_info_for_name_response_instance.to_dict()
# create an instance of GetEventRegistrationInfoForNameResponse from a dict
get_event_registration_info_for_name_response_from_dict = GetEventRegistrationInfoForNameResponse.from_dict(get_event_registration_info_for_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


