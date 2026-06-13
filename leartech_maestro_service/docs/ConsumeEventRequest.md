# ConsumeEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actioned_by** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**produced_time** | **datetime** |  | 

## Example

```python
from leartech_maestro_service.models.consume_event_request import ConsumeEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumeEventRequest from a JSON string
consume_event_request_instance = ConsumeEventRequest.from_json(json)
# print the JSON string representation of the object
print(ConsumeEventRequest.to_json())

# convert the object into a dict
consume_event_request_dict = consume_event_request_instance.to_dict()
# create an instance of ConsumeEventRequest from a dict
consume_event_request_from_dict = ConsumeEventRequest.from_dict(consume_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


