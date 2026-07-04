# ModelsTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_tenant import ModelsTenant

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsTenant from a JSON string
models_tenant_instance = ModelsTenant.from_json(json)
# print the JSON string representation of the object
print(ModelsTenant.to_json())

# convert the object into a dict
models_tenant_dict = models_tenant_instance.to_dict()
# create an instance of ModelsTenant from a dict
models_tenant_from_dict = ModelsTenant.from_dict(models_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


