# HandlersPeerResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_ms** | **int** |  | [optional] 
**http_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**ok** | **bool** |  | [optional] 
**peer** | **str** |  | [optional] 

## Example

```python
from leartech_mortgages_api.models.handlers_peer_result import HandlersPeerResult

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersPeerResult from a JSON string
handlers_peer_result_instance = HandlersPeerResult.from_json(json)
# print the JSON string representation of the object
print(HandlersPeerResult.to_json())

# convert the object into a dict
handlers_peer_result_dict = handlers_peer_result_instance.to_dict()
# create an instance of HandlersPeerResult from a dict
handlers_peer_result_from_dict = HandlersPeerResult.from_dict(handlers_peer_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


