# ModelsAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**requires2fa** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_auth_response import ModelsAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAuthResponse from a JSON string
models_auth_response_instance = ModelsAuthResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsAuthResponse.to_json())

# convert the object into a dict
models_auth_response_dict = models_auth_response_instance.to_dict()
# create an instance of ModelsAuthResponse from a dict
models_auth_response_from_dict = ModelsAuthResponse.from_dict(models_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


