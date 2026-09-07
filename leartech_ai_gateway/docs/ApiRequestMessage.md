# ApiRequestMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**tool_call_id** | **str** |  | [optional] 
**tool_calls** | **object** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_request_message import ApiRequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequestMessage from a JSON string
api_request_message_instance = ApiRequestMessage.from_json(json)
# print the JSON string representation of the object
print(ApiRequestMessage.to_json())

# convert the object into a dict
api_request_message_dict = api_request_message_instance.to_dict()
# create an instance of ApiRequestMessage from a dict
api_request_message_from_dict = ApiRequestMessage.from_dict(api_request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


