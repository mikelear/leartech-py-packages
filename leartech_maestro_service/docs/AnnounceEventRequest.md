# AnnounceEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actioned_by** | **str** | Who actioned the event (userId if applicable - optional) | [optional] 
**annotations** | **Dict[str, str]** | Annotations associated with the event | [optional] 
**name** | **str** | Name of the event to be announced | 
**produced_by** | **str** | Which service produced the event | 

## Example

```python
from leartech_maestro_service.models.announce_event_request import AnnounceEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnounceEventRequest from a JSON string
announce_event_request_instance = AnnounceEventRequest.from_json(json)
# print the JSON string representation of the object
print(AnnounceEventRequest.to_json())

# convert the object into a dict
announce_event_request_dict = announce_event_request_instance.to_dict()
# create an instance of AnnounceEventRequest from a dict
announce_event_request_from_dict = AnnounceEventRequest.from_dict(announce_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


