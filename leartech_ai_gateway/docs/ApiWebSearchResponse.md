# ApiWebSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiWebSearchProvider]**](ApiWebSearchProvider.md) |  | [optional] 
**default** | **str** | the selected provider&#39;s id | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_web_search_response import ApiWebSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWebSearchResponse from a JSON string
api_web_search_response_instance = ApiWebSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ApiWebSearchResponse.to_json())

# convert the object into a dict
api_web_search_response_dict = api_web_search_response_instance.to_dict()
# create an instance of ApiWebSearchResponse from a dict
api_web_search_response_from_dict = ApiWebSearchResponse.from_dict(api_web_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


