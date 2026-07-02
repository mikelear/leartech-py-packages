# ModelsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**role** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_user import ModelsUser

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsUser from a JSON string
models_user_instance = ModelsUser.from_json(json)
# print the JSON string representation of the object
print(ModelsUser.to_json())

# convert the object into a dict
models_user_dict = models_user_instance.to_dict()
# create an instance of ModelsUser from a dict
models_user_from_dict = ModelsUser.from_dict(models_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


