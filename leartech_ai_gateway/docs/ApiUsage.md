# ApiUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_tokens** | **int** |  | [optional] 
**prompt_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_usage import ApiUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsage from a JSON string
api_usage_instance = ApiUsage.from_json(json)
# print the JSON string representation of the object
print(ApiUsage.to_json())

# convert the object into a dict
api_usage_dict = api_usage_instance.to_dict()
# create an instance of ApiUsage from a dict
api_usage_from_dict = ApiUsage.from_dict(api_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


