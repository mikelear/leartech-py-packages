# BlockchainSubmitResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**gas** | **int** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**nonce** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_submit_result import BlockchainSubmitResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainSubmitResult from a JSON string
blockchain_submit_result_instance = BlockchainSubmitResult.from_json(json)
# print the JSON string representation of the object
print(BlockchainSubmitResult.to_json())

# convert the object into a dict
blockchain_submit_result_dict = blockchain_submit_result_instance.to_dict()
# create an instance of BlockchainSubmitResult from a dict
blockchain_submit_result_from_dict = BlockchainSubmitResult.from_dict(blockchain_submit_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


