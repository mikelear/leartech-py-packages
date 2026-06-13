# EventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actioned_by** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**consumptions** | [**List[EventConsumptionDto]**](EventConsumptionDto.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**produced_by** | **str** |  | [optional] 
**produced_time** | **str** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.event_dto import EventDto

# TODO update the JSON string below
json = "{}"
# create an instance of EventDto from a JSON string
event_dto_instance = EventDto.from_json(json)
# print the JSON string representation of the object
print(EventDto.to_json())

# convert the object into a dict
event_dto_dict = event_dto_instance.to_dict()
# create an instance of EventDto from a dict
event_dto_from_dict = EventDto.from_dict(event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


