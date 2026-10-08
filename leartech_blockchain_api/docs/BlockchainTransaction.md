# BlockchainTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**receipt** | **Dict[str, object]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_transaction import BlockchainTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainTransaction from a JSON string
blockchain_transaction_instance = BlockchainTransaction.from_json(json)
# print the JSON string representation of the object
print(BlockchainTransaction.to_json())

# convert the object into a dict
blockchain_transaction_dict = blockchain_transaction_instance.to_dict()
# create an instance of BlockchainTransaction from a dict
blockchain_transaction_from_dict = BlockchainTransaction.from_dict(blockchain_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


