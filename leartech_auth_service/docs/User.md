# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_login_at** | **str** | LastLoginAt is the most recent successful login (password or passkey). Nil when the user has never logged in (e.g. invite-pending). Read-only. | [optional] 
**permissions** | **List[str]** |  | [optional] 
**role** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


