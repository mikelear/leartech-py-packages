# ApiChatCompletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_tokens** | **int** |  | [optional] 
**messages** | [**List[ApiRequestMessage]**](ApiRequestMessage.md) |  | 
**model** | **str** |  | 
**stream** | **bool** |  | [optional] 
**stream_options** | [**ApiStreamOptions**](ApiStreamOptions.md) | StreamOptions.IncludeUsage asks for a final chunk carrying the token and cache breakdown, the same shape OpenAI emits and the same one openai.go already sends UPSTREAM and parses back.  The gateway received usage on every streamed call, billed with it, and dropped it before the client -- so a streamed turn was the least visible traffic on the system while being the highest volume an agent loop produces. Found by the CLI session building the first streaming consumer. | [optional] 
**temperature** | **float** |  | [optional] 
**tool_choice** | **object** |  | [optional] 
**tools** | **object** | S7b passthrough: forwarded verbatim to OpenAI-compatible providers. | [optional] 
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


