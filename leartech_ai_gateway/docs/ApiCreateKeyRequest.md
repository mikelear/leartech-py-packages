# ApiCreateKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_micros** | **int** |  | 
**expires_at** | **str** |  | [optional] 
**model_allowlist** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**rate_limit_rpm** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_create_key_request import ApiCreateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateKeyRequest from a JSON string
api_create_key_request_instance = ApiCreateKeyRequest.from_json(json)
# print the JSON string representation of the object
print(ApiCreateKeyRequest.to_json())

# convert the object into a dict
api_create_key_request_dict = api_create_key_request_instance.to_dict()
# create an instance of ApiCreateKeyRequest from a dict
api_create_key_request_from_dict = ApiCreateKeyRequest.from_dict(api_create_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


