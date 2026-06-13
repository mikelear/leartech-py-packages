# LatestSuccessfulEventConsumptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed_by** | **str** |  | [optional] 
**consumed_time** | **str** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.latest_successful_event_consumption_dto import LatestSuccessfulEventConsumptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of LatestSuccessfulEventConsumptionDto from a JSON string
latest_successful_event_consumption_dto_instance = LatestSuccessfulEventConsumptionDto.from_json(json)
# print the JSON string representation of the object
print(LatestSuccessfulEventConsumptionDto.to_json())

# convert the object into a dict
latest_successful_event_consumption_dto_dict = latest_successful_event_consumption_dto_instance.to_dict()
# create an instance of LatestSuccessfulEventConsumptionDto from a dict
latest_successful_event_consumption_dto_from_dict = LatestSuccessfulEventConsumptionDto.from_dict(latest_successful_event_consumption_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


