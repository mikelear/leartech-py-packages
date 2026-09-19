# ApiTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Available reports whether THIS credential may call it. Unavailable tools are still listed, deliberately: a shortened list makes \&quot;why can this shell not search\&quot; unanswerable without reading scopes by hand.  The client shows the full list and offers only the available ones to the model, so display and capability stay different lists. Offering an unavailable tool would have the model plan around a capability it does not have and then 403. | [optional] 
**function** | [**ApiToolFunction**](ApiToolFunction.md) |  | [optional] 
**scope** | **str** | Scope names what a caller would need, so \&quot;unavailable\&quot; is actionable rather than just a closed door. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_tool import ApiTool

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTool from a JSON string
api_tool_instance = ApiTool.from_json(json)
# print the JSON string representation of the object
print(ApiTool.to_json())

# convert the object into a dict
api_tool_dict = api_tool_instance.to_dict()
# create an instance of ApiTool from a dict
api_tool_from_dict = ApiTool.from_dict(api_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


