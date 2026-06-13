# ConsumeEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** |  | [optional] 
**is_consumed** | **bool** |  | [optional] 
**is_errored** | **bool** |  | [optional] 

## Example

```python
from leartech_maestro_service.models.consume_event_response import ConsumeEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumeEventResponse from a JSON string
consume_event_response_instance = ConsumeEventResponse.from_json(json)
# print the JSON string representation of the object
print(ConsumeEventResponse.to_json())

# convert the object into a dict
consume_event_response_dict = consume_event_response_instance.to_dict()
# create an instance of ConsumeEventResponse from a dict
consume_event_response_from_dict = ConsumeEventResponse.from_dict(consume_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


