# EventRegistrationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumers** | [**List[Consumer]**](Consumer.md) |  | [optional] 
**name** | **str** |  | [optional] 
**producer** | [**Producer**](Producer.md) |  | [optional] 

## Example

```python
from leartech_maestro_service.models.event_registration_info import EventRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EventRegistrationInfo from a JSON string
event_registration_info_instance = EventRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print(EventRegistrationInfo.to_json())

# convert the object into a dict
event_registration_info_dict = event_registration_info_instance.to_dict()
# create an instance of EventRegistrationInfo from a dict
event_registration_info_from_dict = EventRegistrationInfo.from_dict(event_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


