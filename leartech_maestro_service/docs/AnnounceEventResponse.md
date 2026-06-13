# AnnounceEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** |  | [optional] 
**received** | **bool** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.announce_event_response import AnnounceEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnounceEventResponse from a JSON string
announce_event_response_instance = AnnounceEventResponse.from_json(json)
# print the JSON string representation of the object
print(AnnounceEventResponse.to_json())

# convert the object into a dict
announce_event_response_dict = announce_event_response_instance.to_dict()
# create an instance of AnnounceEventResponse from a dict
announce_event_response_from_dict = AnnounceEventResponse.from_dict(announce_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


