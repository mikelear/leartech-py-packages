# GetLatestEventsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** |  | [optional] 
**latest_events** | [**List[LatestEventDto]**](LatestEventDto.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.get_latest_events_details_response import GetLatestEventsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestEventsDetailsResponse from a JSON string
get_latest_events_details_response_instance = GetLatestEventsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetLatestEventsDetailsResponse.to_json())

# convert the object into a dict
get_latest_events_details_response_dict = get_latest_events_details_response_instance.to_dict()
# create an instance of GetLatestEventsDetailsResponse from a dict
get_latest_events_details_response_from_dict = GetLatestEventsDetailsResponse.from_dict(get_latest_events_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


