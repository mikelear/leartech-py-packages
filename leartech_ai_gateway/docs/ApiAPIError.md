# ApiAPIError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_api_error import ApiAPIError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAPIError from a JSON string
api_api_error_instance = ApiAPIError.from_json(json)
# print the JSON string representation of the object
print(ApiAPIError.to_json())

# convert the object into a dict
api_api_error_dict = api_api_error_instance.to_dict()
# create an instance of ApiAPIError from a dict
api_api_error_from_dict = ApiAPIError.from_dict(api_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


