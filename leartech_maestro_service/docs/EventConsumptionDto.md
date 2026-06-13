# EventConsumptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed_by** | **str** |  | [optional] 
**consumed_time** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**is_consumed** | **bool** |  | [optional] 
**is_errored** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.event_consumption_dto import EventConsumptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of EventConsumptionDto from a JSON string
event_consumption_dto_instance = EventConsumptionDto.from_json(json)
# print the JSON string representation of the object
print(EventConsumptionDto.to_json())

# convert the object into a dict
event_consumption_dto_dict = event_consumption_dto_instance.to_dict()
# create an instance of EventConsumptionDto from a dict
event_consumption_dto_from_dict = EventConsumptionDto.from_dict(event_consumption_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


