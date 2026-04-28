# ModelsTwoFactorEnableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qr_code_url** | **str** |  | [optional] 
**recovery_codes** | **List[str]** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_two_factor_enable_response import ModelsTwoFactorEnableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsTwoFactorEnableResponse from a JSON string
models_two_factor_enable_response_instance = ModelsTwoFactorEnableResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsTwoFactorEnableResponse.to_json())

# convert the object into a dict
models_two_factor_enable_response_dict = models_two_factor_enable_response_instance.to_dict()
# create an instance of ModelsTwoFactorEnableResponse from a dict
models_two_factor_enable_response_from_dict = ModelsTwoFactorEnableResponse.from_dict(models_two_factor_enable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


