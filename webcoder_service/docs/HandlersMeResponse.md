# HandlersMeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from webcoder_service.models.handlers_me_response import HandlersMeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersMeResponse from a JSON string
handlers_me_response_instance = HandlersMeResponse.from_json(json)
# print the JSON string representation of the object
print(HandlersMeResponse.to_json())

# convert the object into a dict
handlers_me_response_dict = handlers_me_response_instance.to_dict()
# create an instance of HandlersMeResponse from a dict
handlers_me_response_from_dict = HandlersMeResponse.from_dict(handlers_me_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


