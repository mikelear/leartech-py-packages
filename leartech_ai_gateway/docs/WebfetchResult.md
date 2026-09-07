# WebfetchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**final_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**truncated** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.webfetch_result import WebfetchResult

# TODO update the JSON string below
json = "{}"
# create an instance of WebfetchResult from a JSON string
webfetch_result_instance = WebfetchResult.from_json(json)
# print the JSON string representation of the object
print(WebfetchResult.to_json())

# convert the object into a dict
webfetch_result_dict = webfetch_result_instance.to_dict()
# create an instance of WebfetchResult from a dict
webfetch_result_from_dict = WebfetchResult.from_dict(webfetch_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


