# GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse


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
from leartech_auth_service.models.github_com_mikelear_leartech_auth_service_internal_models_auth_response import GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse from a JSON string
github_com_mikelear_leartech_auth_service_internal_models_auth_response_instance = GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse.to_json())

# convert the object into a dict
github_com_mikelear_leartech_auth_service_internal_models_auth_response_dict = github_com_mikelear_leartech_auth_service_internal_models_auth_response_instance.to_dict()
# create an instance of GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse from a dict
github_com_mikelear_leartech_auth_service_internal_models_auth_response_from_dict = GithubComMikelearLeartechAuthServiceInternalModelsAuthResponse.from_dict(github_com_mikelear_leartech_auth_service_internal_models_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


