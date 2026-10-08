# BlockchainReadResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**decoded** | **Dict[str, object]** |  | [optional] 
**method** | **str** |  | [optional] 
**raw** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_read_result import BlockchainReadResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainReadResult from a JSON string
blockchain_read_result_instance = BlockchainReadResult.from_json(json)
# print the JSON string representation of the object
print(BlockchainReadResult.to_json())

# convert the object into a dict
blockchain_read_result_dict = blockchain_read_result_instance.to_dict()
# create an instance of BlockchainReadResult from a dict
blockchain_read_result_from_dict = BlockchainReadResult.from_dict(blockchain_read_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


