# ApiListKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[ApiKeyView]**](ApiKeyView.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_list_keys_response import ApiListKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListKeysResponse from a JSON string
api_list_keys_response_instance = ApiListKeysResponse.from_json(json)
# print the JSON string representation of the object
print(ApiListKeysResponse.to_json())

# convert the object into a dict
api_list_keys_response_dict = api_list_keys_response_instance.to_dict()
# create an instance of ApiListKeysResponse from a dict
api_list_keys_response_from_dict = ApiListKeysResponse.from_dict(api_list_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


