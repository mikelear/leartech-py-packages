# LatestFailedEventConsumptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed_by** | **str** |  | [optional] 
**consumed_time** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.latest_failed_event_consumption_dto import LatestFailedEventConsumptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of LatestFailedEventConsumptionDto from a JSON string
latest_failed_event_consumption_dto_instance = LatestFailedEventConsumptionDto.from_json(json)
# print the JSON string representation of the object
print(LatestFailedEventConsumptionDto.to_json())

# convert the object into a dict
latest_failed_event_consumption_dto_dict = latest_failed_event_consumption_dto_instance.to_dict()
# create an instance of LatestFailedEventConsumptionDto from a dict
latest_failed_event_consumption_dto_from_dict = LatestFailedEventConsumptionDto.from_dict(latest_failed_event_consumption_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


