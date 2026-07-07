# AdminUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**has2_fa** | **bool** |  | [optional] 
**has_passkey** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**role** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.admin_user_response import AdminUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserResponse from a JSON string
admin_user_response_instance = AdminUserResponse.from_json(json)
# print the JSON string representation of the object
print(AdminUserResponse.to_json())

# convert the object into a dict
admin_user_response_dict = admin_user_response_instance.to_dict()
# create an instance of AdminUserResponse from a dict
admin_user_response_from_dict = AdminUserResponse.from_dict(admin_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


