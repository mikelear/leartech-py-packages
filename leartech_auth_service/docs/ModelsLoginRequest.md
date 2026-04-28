# ModelsLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from leartech_auth_service.models.models_login_request import ModelsLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsLoginRequest from a JSON string
models_login_request_instance = ModelsLoginRequest.from_json(json)
# print the JSON string representation of the object
print(ModelsLoginRequest.to_json())

# convert the object into a dict
models_login_request_dict = models_login_request_instance.to_dict()
# create an instance of ModelsLoginRequest from a dict
models_login_request_from_dict = ModelsLoginRequest.from_dict(models_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


