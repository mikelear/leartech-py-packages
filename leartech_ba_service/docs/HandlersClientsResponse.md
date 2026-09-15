# HandlersClientsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksums_url** | **str** |  | [optional] 
**clients** | [**List[HandlersClientBinary]**](HandlersClientBinary.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from leartech_ba_service.models.handlers_clients_response import HandlersClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersClientsResponse from a JSON string
handlers_clients_response_instance = HandlersClientsResponse.from_json(json)
# print the JSON string representation of the object
print(HandlersClientsResponse.to_json())

# convert the object into a dict
handlers_clients_response_dict = handlers_clients_response_instance.to_dict()
# create an instance of HandlersClientsResponse from a dict
handlers_clients_response_from_dict = HandlersClientsResponse.from_dict(handlers_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


