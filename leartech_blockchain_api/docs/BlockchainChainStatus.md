# BlockchainChainStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_height** | **int** |  | [optional] 
**chain_id** | **int** |  | [optional] 
**connected** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_chain_status import BlockchainChainStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainChainStatus from a JSON string
blockchain_chain_status_instance = BlockchainChainStatus.from_json(json)
# print the JSON string representation of the object
print(BlockchainChainStatus.to_json())

# convert the object into a dict
blockchain_chain_status_dict = blockchain_chain_status_instance.to_dict()
# create an instance of BlockchainChainStatus from a dict
blockchain_chain_status_from_dict = BlockchainChainStatus.from_dict(blockchain_chain_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


