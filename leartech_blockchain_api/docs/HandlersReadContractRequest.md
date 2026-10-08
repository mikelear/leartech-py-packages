# HandlersReadContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[object]** |  | [optional] 
**method** | **str** |  | 

## Example

```python
from leartech_blockchain_api.models.handlers_read_contract_request import HandlersReadContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersReadContractRequest from a JSON string
handlers_read_contract_request_instance = HandlersReadContractRequest.from_json(json)
# print the JSON string representation of the object
print(HandlersReadContractRequest.to_json())

# convert the object into a dict
handlers_read_contract_request_dict = handlers_read_contract_request_instance.to_dict()
# create an instance of HandlersReadContractRequest from a dict
handlers_read_contract_request_from_dict = HandlersReadContractRequest.from_dict(handlers_read_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


