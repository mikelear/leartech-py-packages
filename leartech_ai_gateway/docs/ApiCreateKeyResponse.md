# ApiCreateKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ApiKeyView**](ApiKeyView.md) |  | [optional] 
**keyid** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_create_key_response import ApiCreateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateKeyResponse from a JSON string
api_create_key_response_instance = ApiCreateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ApiCreateKeyResponse.to_json())

# convert the object into a dict
api_create_key_response_dict = api_create_key_response_instance.to_dict()
# create an instance of ApiCreateKeyResponse from a dict
api_create_key_response_from_dict = ApiCreateKeyResponse.from_dict(api_create_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


