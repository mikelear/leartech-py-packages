# ApiChatCompletionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[ApiChoice]**](ApiChoice.md) |  | [optional] 
**created** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**usage** | [**ApiUsage**](ApiUsage.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_chat_completion_response import ApiChatCompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatCompletionResponse from a JSON string
api_chat_completion_response_instance = ApiChatCompletionResponse.from_json(json)
# print the JSON string representation of the object
print(ApiChatCompletionResponse.to_json())

# convert the object into a dict
api_chat_completion_response_dict = api_chat_completion_response_instance.to_dict()
# create an instance of ApiChatCompletionResponse from a dict
api_chat_completion_response_from_dict = ApiChatCompletionResponse.from_dict(api_chat_completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


