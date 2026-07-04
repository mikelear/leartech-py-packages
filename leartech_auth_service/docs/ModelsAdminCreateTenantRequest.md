# ModelsAdminCreateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from leartech_auth_service.models.models_admin_create_tenant_request import ModelsAdminCreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAdminCreateTenantRequest from a JSON string
models_admin_create_tenant_request_instance = ModelsAdminCreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsAdminCreateTenantRequest.to_json())

# convert the object into a dict
models_admin_create_tenant_request_dict = models_admin_create_tenant_request_instance.to_dict()
# create an instance of ModelsAdminCreateTenantRequest from a dict
models_admin_create_tenant_request_from_dict = ModelsAdminCreateTenantRequest.from_dict(models_admin_create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


