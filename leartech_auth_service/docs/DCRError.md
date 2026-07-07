# DCRError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.dcr_error import DCRError

# TODO update the JSON string below
json = "{}"
# create an instance of DCRError from a JSON string
dcr_error_instance = DCRError.from_json(json)
# print the JSON string representation of the object
print(DCRError.to_json())

# convert the object into a dict
dcr_error_dict = dcr_error_instance.to_dict()
# create an instance of DCRError from a dict
dcr_error_from_dict = DCRError.from_dict(dcr_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


