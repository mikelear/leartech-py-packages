# HandlersClientBinary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**bytes** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from leartech_ba_service.models.handlers_client_binary import HandlersClientBinary

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersClientBinary from a JSON string
handlers_client_binary_instance = HandlersClientBinary.from_json(json)
# print the JSON string representation of the object
print(HandlersClientBinary.to_json())

# convert the object into a dict
handlers_client_binary_dict = handlers_client_binary_instance.to_dict()
# create an instance of HandlersClientBinary from a dict
handlers_client_binary_from_dict = HandlersClientBinary.from_dict(handlers_client_binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


