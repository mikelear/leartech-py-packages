# ApiChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_chat_message import ApiChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatMessage from a JSON string
api_chat_message_instance = ApiChatMessage.from_json(json)
# print the JSON string representation of the object
print(ApiChatMessage.to_json())

# convert the object into a dict
api_chat_message_dict = api_chat_message_instance.to_dict()
# create an instance of ApiChatMessage from a dict
api_chat_message_from_dict = ApiChatMessage.from_dict(api_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


