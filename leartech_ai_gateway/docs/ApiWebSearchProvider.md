# ApiWebSearchProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Default is the provider used when a request omits &#x60;provider&#x60;. | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | the &#x60;provider&#x60; value a request sends | [optional] 
**keyless** | **bool** | Keyless reports whether this provider runs with no third-party credential (searxng aggregates keyless engines) — the \&quot;open lane\&quot; vs the \&quot;curated lane\&quot; a caller may be choosing between. | [optional] 
**name** | **str** | human-facing | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_web_search_provider import ApiWebSearchProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWebSearchProvider from a JSON string
api_web_search_provider_instance = ApiWebSearchProvider.from_json(json)
# print the JSON string representation of the object
print(ApiWebSearchProvider.to_json())

# convert the object into a dict
api_web_search_provider_dict = api_web_search_provider_instance.to_dict()
# create an instance of ApiWebSearchProvider from a dict
api_web_search_provider_from_dict = ApiWebSearchProvider.from_dict(api_web_search_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


