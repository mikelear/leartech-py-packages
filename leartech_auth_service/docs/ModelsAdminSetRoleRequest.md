# ModelsAdminSetRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from leartech_auth_service.models.models_admin_set_role_request import ModelsAdminSetRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAdminSetRoleRequest from a JSON string
models_admin_set_role_request_instance = ModelsAdminSetRoleRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsAdminSetRoleRequest.to_json())

# convert the object into a dict
models_admin_set_role_request_dict = models_admin_set_role_request_instance.to_dict()
# create an instance of ModelsAdminSetRoleRequest from a dict
models_admin_set_role_request_from_dict = ModelsAdminSetRoleRequest.from_dict(models_admin_set_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


