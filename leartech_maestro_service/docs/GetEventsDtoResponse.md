# GetEventsDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** |  | [optional] 
**events** | [**List[EventDto]**](EventDto.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.get_events_dto_response import GetEventsDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsDtoResponse from a JSON string
get_events_dto_response_instance = GetEventsDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventsDtoResponse.to_json())

# convert the object into a dict
get_events_dto_response_dict = get_events_dto_response_instance.to_dict()
# create an instance of GetEventsDtoResponse from a dict
get_events_dto_response_from_dict = GetEventsDtoResponse.from_dict(get_events_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


