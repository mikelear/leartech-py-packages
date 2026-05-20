# HandlersFleetTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HandlersPeerResult]**](HandlersPeerResult.md) |  | [optional] 
**success** | **bool** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from leartech_mortgages_api.models.handlers_fleet_test_response import HandlersFleetTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersFleetTestResponse from a JSON string
handlers_fleet_test_response_instance = HandlersFleetTestResponse.from_json(json)
# print the JSON string representation of the object
print(HandlersFleetTestResponse.to_json())

# convert the object into a dict
handlers_fleet_test_response_dict = handlers_fleet_test_response_instance.to_dict()
# create an instance of HandlersFleetTestResponse from a dict
handlers_fleet_test_response_from_dict = HandlersFleetTestResponse.from_dict(handlers_fleet_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


