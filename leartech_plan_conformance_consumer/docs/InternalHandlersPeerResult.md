# InternalHandlersPeerResult


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
from leartech_plan_conformance_consumer.models.internal_handlers_peer_result import InternalHandlersPeerResult

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlersPeerResult from a JSON string
internal_handlers_peer_result_instance = InternalHandlersPeerResult.from_json(json)
# print the JSON string representation of the object
print(InternalHandlersPeerResult.to_json())

# convert the object into a dict
internal_handlers_peer_result_dict = internal_handlers_peer_result_instance.to_dict()
# create an instance of InternalHandlersPeerResult from a dict
internal_handlers_peer_result_from_dict = InternalHandlersPeerResult.from_dict(internal_handlers_peer_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


