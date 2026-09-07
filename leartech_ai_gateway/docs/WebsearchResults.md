# WebsearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | synthesized answer when the provider offers one (Tavily) | [optional] 
**provider** | **str** |  | [optional] 
**results** | [**List[WebsearchItem]**](WebsearchItem.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.websearch_results import WebsearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of WebsearchResults from a JSON string
websearch_results_instance = WebsearchResults.from_json(json)
# print the JSON string representation of the object
print(WebsearchResults.to_json())

# convert the object into a dict
websearch_results_dict = websearch_results_instance.to_dict()
# create an instance of WebsearchResults from a dict
websearch_results_from_dict = WebsearchResults.from_dict(websearch_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


