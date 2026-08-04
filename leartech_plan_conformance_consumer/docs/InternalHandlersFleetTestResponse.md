# InternalHandlersFleetTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InternalHandlersPeerResult]**](InternalHandlersPeerResult.md) |  | [optional] 
**success** | **bool** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from leartech_plan_conformance_consumer.models.internal_handlers_fleet_test_response import InternalHandlersFleetTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlersFleetTestResponse from a JSON string
internal_handlers_fleet_test_response_instance = InternalHandlersFleetTestResponse.from_json(json)
# print the JSON string representation of the object
print(InternalHandlersFleetTestResponse.to_json())

# convert the object into a dict
internal_handlers_fleet_test_response_dict = internal_handlers_fleet_test_response_instance.to_dict()
# create an instance of InternalHandlersFleetTestResponse from a dict
internal_handlers_fleet_test_response_from_dict = InternalHandlersFleetTestResponse.from_dict(internal_handlers_fleet_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


