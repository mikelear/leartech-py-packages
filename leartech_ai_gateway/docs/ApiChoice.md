# ApiChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_reason** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**message** | [**ApiChatMessage**](ApiChatMessage.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_choice import ApiChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChoice from a JSON string
api_choice_instance = ApiChoice.from_json(json)
# print the JSON string representation of the object
print(ApiChoice.to_json())

# convert the object into a dict
api_choice_dict = api_choice_instance.to_dict()
# create an instance of ApiChoice from a dict
api_choice_from_dict = ApiChoice.from_dict(api_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


