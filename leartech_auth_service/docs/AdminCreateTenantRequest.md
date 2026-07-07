# AdminCreateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from leartech_auth_service.models.admin_create_tenant_request import AdminCreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCreateTenantRequest from a JSON string
admin_create_tenant_request_instance = AdminCreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(AdminCreateTenantRequest.to_json())

# convert the object into a dict
admin_create_tenant_request_dict = admin_create_tenant_request_instance.to_dict()
# create an instance of AdminCreateTenantRequest from a dict
admin_create_tenant_request_from_dict = AdminCreateTenantRequest.from_dict(admin_create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


