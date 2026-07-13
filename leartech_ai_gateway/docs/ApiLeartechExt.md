# ApiLeartechExt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_residency** | **str** |  | [optional] 
**routing_hint** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_leartech_ext import ApiLeartechExt

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLeartechExt from a JSON string
api_leartech_ext_instance = ApiLeartechExt.from_json(json)
# print the JSON string representation of the object
print(ApiLeartechExt.to_json())

# convert the object into a dict
api_leartech_ext_dict = api_leartech_ext_instance.to_dict()
# create an instance of ApiLeartechExt from a dict
api_leartech_ext_from_dict = ApiLeartechExt.from_dict(api_leartech_ext_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


