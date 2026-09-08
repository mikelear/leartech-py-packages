# ApiKeyView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_micros** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**keyid** | **str** |  | [optional] 
**last_used_at** | **str** |  | [optional] 
**model_allowlist** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**rate_limit_rpm** | **int** |  | [optional] 
**revoked_at** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_key_view import ApiKeyView

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyView from a JSON string
api_key_view_instance = ApiKeyView.from_json(json)
# print the JSON string representation of the object
print(ApiKeyView.to_json())

# convert the object into a dict
api_key_view_dict = api_key_view_instance.to_dict()
# create an instance of ApiKeyView from a dict
api_key_view_from_dict = ApiKeyView.from_dict(api_key_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


