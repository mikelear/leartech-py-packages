# AdminSetRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from leartech_auth_service.models.admin_set_role_request import AdminSetRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetRoleRequest from a JSON string
admin_set_role_request_instance = AdminSetRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AdminSetRoleRequest.to_json())

# convert the object into a dict
admin_set_role_request_dict = admin_set_role_request_instance.to_dict()
# create an instance of AdminSetRoleRequest from a dict
admin_set_role_request_from_dict = AdminSetRoleRequest.from_dict(admin_set_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


