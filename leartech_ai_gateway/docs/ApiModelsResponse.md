# ApiModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiModel]**](ApiModel.md) |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_models_response import ApiModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiModelsResponse from a JSON string
api_models_response_instance = ApiModelsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiModelsResponse.to_json())

# convert the object into a dict
api_models_response_dict = api_models_response_instance.to_dict()
# create an instance of ApiModelsResponse from a dict
api_models_response_from_dict = ApiModelsResponse.from_dict(api_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


