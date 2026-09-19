# ApiToolFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is what the model chooses on AND what a user reads at approval time, so it is written for both. | [optional] 
**name** | **str** |  | [optional] 
**parameters** | **object** | Parameters is a JSON Schema, kept RAW for the same reason ToolCall.Arguments is: the gateway publishes it without interpreting it, so a schema keyword we do not model survives translation. | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_tool_function import ApiToolFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToolFunction from a JSON string
api_tool_function_instance = ApiToolFunction.from_json(json)
# print the JSON string representation of the object
print(ApiToolFunction.to_json())

# convert the object into a dict
api_tool_function_dict = api_tool_function_instance.to_dict()
# create an instance of ApiToolFunction from a dict
api_tool_function_from_dict = ApiToolFunction.from_dict(api_tool_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


