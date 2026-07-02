# ModelsDCRRegisterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_id_issued_at** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**client_secret_expires_at** | **int** |  | [optional] 
**grant_types** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**response_types** | **List[str]** |  | [optional] 
**scope** | **str** |  | [optional] 
**software_id** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_dcr_register_response import ModelsDCRRegisterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsDCRRegisterResponse from a JSON string
models_dcr_register_response_instance = ModelsDCRRegisterResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsDCRRegisterResponse.to_json())

# convert the object into a dict
models_dcr_register_response_dict = models_dcr_register_response_instance.to_dict()
# create an instance of ModelsDCRRegisterResponse from a dict
models_dcr_register_response_from_dict = ModelsDCRRegisterResponse.from_dict(models_dcr_register_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


