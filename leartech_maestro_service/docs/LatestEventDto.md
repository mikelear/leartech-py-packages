# LatestEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_failed_consumptions** | [**List[LatestFailedEventConsumptionDto]**](LatestFailedEventConsumptionDto.md) |  | [optional] 
**latest_successful_consumptions** | [**List[LatestSuccessfulEventConsumptionDto]**](LatestSuccessfulEventConsumptionDto.md) |  | [optional] 
**name** | **str** |  | [optional] 
**produced_by** | **str** |  | [optional] 
**produced_time** | **str** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.latest_event_dto import LatestEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of LatestEventDto from a JSON string
latest_event_dto_instance = LatestEventDto.from_json(json)
# print the JSON string representation of the object
print(LatestEventDto.to_json())

# convert the object into a dict
latest_event_dto_dict = latest_event_dto_instance.to_dict()
# create an instance of LatestEventDto from a dict
latest_event_dto_from_dict = LatestEventDto.from_dict(latest_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


