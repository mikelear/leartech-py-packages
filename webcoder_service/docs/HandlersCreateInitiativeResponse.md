# HandlersCreateInitiativeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 
**var_self** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from webcoder_service.models.handlers_create_initiative_response import HandlersCreateInitiativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersCreateInitiativeResponse from a JSON string
handlers_create_initiative_response_instance = HandlersCreateInitiativeResponse.from_json(json)
# print the JSON string representation of the object
print(HandlersCreateInitiativeResponse.to_json())

# convert the object into a dict
handlers_create_initiative_response_dict = handlers_create_initiative_response_instance.to_dict()
# create an instance of HandlersCreateInitiativeResponse from a dict
handlers_create_initiative_response_from_dict = HandlersCreateInitiativeResponse.from_dict(handlers_create_initiative_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


