# ApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**max_ctx** | **int** | Capabilities/limits so callers can cap what they can&#39;t otherwise see (INTERFACES.md §4 \&quot;degrade visibly, never silently\&quot;). max_ctx is the model&#39;s context window; vision reports image-input support. | [optional] 
**object** | **str** |  | [optional] 
**owned_by** | **str** |  | [optional] 
**vision** | **bool** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_model import ApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiModel from a JSON string
api_model_instance = ApiModel.from_json(json)
# print the JSON string representation of the object
print(ApiModel.to_json())

# convert the object into a dict
api_model_dict = api_model_instance.to_dict()
# create an instance of ApiModel from a dict
api_model_from_dict = ApiModel.from_dict(api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


