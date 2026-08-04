# MaestroConsumeEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** | ErrorReason is a human-readable description when IsErrored is true or when the event was dropped for a non-error reason (unknown event, malformed body). | [optional] 
**is_consumed** | **bool** | IsConsumed is true when the event was successfully handled. Maestro treats IsConsumed&#x3D;true (regardless of HTTP status) as \&quot;settled, do not retry\&quot;. | [optional] 
**is_errored** | **bool** | IsErrored is true when handler execution failed. Distinct from !IsConsumed so we can signal \&quot;no handler registered\&quot; (neither consumed nor errored) vs. \&quot;handler ran and blew up\&quot; (errored). | [optional] 

## Example

```python
from leartech_plan_conformance_consumer.models.maestro_consume_event_response import MaestroConsumeEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaestroConsumeEventResponse from a JSON string
maestro_consume_event_response_instance = MaestroConsumeEventResponse.from_json(json)
# print the JSON string representation of the object
print(MaestroConsumeEventResponse.to_json())

# convert the object into a dict
maestro_consume_event_response_dict = maestro_consume_event_response_instance.to_dict()
# create an instance of MaestroConsumeEventResponse from a dict
maestro_consume_event_response_from_dict = MaestroConsumeEventResponse.from_dict(maestro_consume_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


