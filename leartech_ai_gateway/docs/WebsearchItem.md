# WebsearchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.websearch_item import WebsearchItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebsearchItem from a JSON string
websearch_item_instance = WebsearchItem.from_json(json)
# print the JSON string representation of the object
print(WebsearchItem.to_json())

# convert the object into a dict
websearch_item_dict = websearch_item_instance.to_dict()
# create an instance of WebsearchItem from a dict
websearch_item_from_dict = WebsearchItem.from_dict(websearch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


