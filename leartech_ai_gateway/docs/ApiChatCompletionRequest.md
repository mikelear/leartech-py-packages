# ApiChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_tokens** | **int** |  | [optional] 
**messages** | [**List[ApiChatMessage]**](ApiChatMessage.md) |  | 
**model** | **str** |  | 
**stream** | **bool** |  | [optional] 
**temperature** | **float** |  | [optional] 
**x_leartech** | [**ApiLeartechExt**](ApiLeartechExt.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_chat_completion_request import ApiChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatCompletionRequest from a JSON string
api_chat_completion_request_instance = ApiChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(ApiChatCompletionRequest.to_json())

# convert the object into a dict
api_chat_completion_request_dict = api_chat_completion_request_instance.to_dict()
# create an instance of ApiChatCompletionRequest from a dict
api_chat_completion_request_from_dict = ApiChatCompletionRequest.from_dict(api_chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


