# GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse


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
from leartech_auth_service.models.github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response import GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse from a JSON string
github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response_instance = GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse.to_json())

# convert the object into a dict
github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response_dict = github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response_instance.to_dict()
# create an instance of GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse from a dict
github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response_from_dict = GithubComMikelearLeartechAuthServiceInternalModelsDCRRegisterResponse.from_dict(github_com_mikelear_leartech_auth_service_internal_models_dcr_register_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


