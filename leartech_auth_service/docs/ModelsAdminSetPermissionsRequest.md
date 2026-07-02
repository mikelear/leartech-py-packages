# ModelsAdminSetPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_admin_set_permissions_request import ModelsAdminSetPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAdminSetPermissionsRequest from a JSON string
models_admin_set_permissions_request_instance = ModelsAdminSetPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsAdminSetPermissionsRequest.to_json())

# convert the object into a dict
models_admin_set_permissions_request_dict = models_admin_set_permissions_request_instance.to_dict()
# create an instance of ModelsAdminSetPermissionsRequest from a dict
models_admin_set_permissions_request_from_dict = ModelsAdminSetPermissionsRequest.from_dict(models_admin_set_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


