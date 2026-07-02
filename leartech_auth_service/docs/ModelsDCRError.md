# ModelsDCRError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.models_dcr_error import ModelsDCRError

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsDCRError from a JSON string
models_dcr_error_instance = ModelsDCRError.from_json(json)
# print the JSON string representation of the object
print(ModelsDCRError.to_json())

# convert the object into a dict
models_dcr_error_dict = models_dcr_error_instance.to_dict()
# create an instance of ModelsDCRError from a dict
models_dcr_error_from_dict = ModelsDCRError.from_dict(models_dcr_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


