# AdminUpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.admin_update_user_request import AdminUpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUpdateUserRequest from a JSON string
admin_update_user_request_instance = AdminUpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(AdminUpdateUserRequest.to_json())

# convert the object into a dict
admin_update_user_request_dict = admin_update_user_request_instance.to_dict()
# create an instance of AdminUpdateUserRequest from a dict
admin_update_user_request_from_dict = AdminUpdateUserRequest.from_dict(admin_update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


