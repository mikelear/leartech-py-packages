# ModelsDCRRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** |  | [optional] 
**contacts** | **List[str]** |  | [optional] 
**grant_types** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**response_types** | **List[str]** |  | [optional] 
**scope** | **str** |  | [optional] 
**software_id** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_dcr_register_request import ModelsDCRRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsDCRRegisterRequest from a JSON string
models_dcr_register_request_instance = ModelsDCRRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsDCRRegisterRequest.to_json())

# convert the object into a dict
models_dcr_register_request_dict = models_dcr_register_request_instance.to_dict()
# create an instance of ModelsDCRRegisterRequest from a dict
models_dcr_register_request_from_dict = ModelsDCRRegisterRequest.from_dict(models_dcr_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


