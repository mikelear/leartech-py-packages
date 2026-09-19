# ApiToolsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiTool]**](ApiTool.md) |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_tools_response import ApiToolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToolsResponse from a JSON string
api_tools_response_instance = ApiToolsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiToolsResponse.to_json())

# convert the object into a dict
api_tools_response_dict = api_tools_response_instance.to_dict()
# create an instance of ApiToolsResponse from a dict
api_tools_response_from_dict = ApiToolsResponse.from_dict(api_tools_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


