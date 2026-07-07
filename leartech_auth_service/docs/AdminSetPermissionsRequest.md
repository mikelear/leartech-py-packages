# AdminSetPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from leartech_auth_service.models.admin_set_permissions_request import AdminSetPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetPermissionsRequest from a JSON string
admin_set_permissions_request_instance = AdminSetPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(AdminSetPermissionsRequest.to_json())

# convert the object into a dict
admin_set_permissions_request_dict = admin_set_permissions_request_instance.to_dict()
# create an instance of AdminSetPermissionsRequest from a dict
admin_set_permissions_request_from_dict = AdminSetPermissionsRequest.from_dict(admin_set_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


