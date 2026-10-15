# BlockchainSubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[object]** |  | [optional] 
**contract** | **str** | Either Contract+Method+Args (an ABI-encoded call on a catalogued contract) or To+Data (raw calldata). | [optional] 
**data** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**value** | **str** | decimal wei | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_submit_request import BlockchainSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainSubmitRequest from a JSON string
blockchain_submit_request_instance = BlockchainSubmitRequest.from_json(json)
# print the JSON string representation of the object
print(BlockchainSubmitRequest.to_json())

# convert the object into a dict
blockchain_submit_request_dict = blockchain_submit_request_instance.to_dict()
# create an instance of BlockchainSubmitRequest from a dict
blockchain_submit_request_from_dict = BlockchainSubmitRequest.from_dict(blockchain_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


