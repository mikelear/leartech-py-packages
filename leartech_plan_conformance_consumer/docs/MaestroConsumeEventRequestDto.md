# MaestroConsumeEventRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actioned_by** | **str** | ActionedBy is the userId (or system-actor id) from the announcement, when present. | [optional] 
**annotations** | **Dict[str, str]** | Annotations are the string k/v pairs from the announcement. Same vocabulary as pkg/maestro.Event.Annotations on the producer side. | [optional] 
**id** | **str** | ID is the unique event id Maestro assigned at announce time. | [optional] 
**name** | **str** | Name is the dotted event name — the dispatch key. | [optional] 
**produced_time** | **str** | ProducedTime is the RFC3339 timestamp of the original announcement. Maestro emits an RFC3339 string; we decode with time.Time so downstream handlers get a native value. | [optional] 

## Example

```python
from leartech_plan_conformance_consumer.models.maestro_consume_event_request_dto import MaestroConsumeEventRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MaestroConsumeEventRequestDto from a JSON string
maestro_consume_event_request_dto_instance = MaestroConsumeEventRequestDto.from_json(json)
# print the JSON string representation of the object
print(MaestroConsumeEventRequestDto.to_json())

# convert the object into a dict
maestro_consume_event_request_dto_dict = maestro_consume_event_request_dto_instance.to_dict()
# create an instance of MaestroConsumeEventRequestDto from a dict
maestro_consume_event_request_dto_from_dict = MaestroConsumeEventRequestDto.from_dict(maestro_consume_event_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


