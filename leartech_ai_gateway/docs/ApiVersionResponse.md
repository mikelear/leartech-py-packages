# ApiVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_level** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_version_response import ApiVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiVersionResponse from a JSON string
api_version_response_instance = ApiVersionResponse.from_json(json)
# print the JSON string representation of the object
print(ApiVersionResponse.to_json())

# convert the object into a dict
api_version_response_dict = api_version_response_instance.to_dict()
# create an instance of ApiVersionResponse from a dict
api_version_response_from_dict = ApiVersionResponse.from_dict(api_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


