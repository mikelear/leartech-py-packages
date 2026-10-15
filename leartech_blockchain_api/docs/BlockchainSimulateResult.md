# BlockchainSimulateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decoded** | **Dict[str, object]** |  | [optional] 
**var_from** | **str** |  | [optional] 
**gas_estimate** | **int** |  | [optional] 
**gas_source** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**raw** | **str** |  | [optional] 
**revert_reason** | **str** |  | [optional] 
**reverted** | **bool** |  | [optional] 
**to** | **str** |  | [optional] 
**trace** | **Dict[str, object]** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_simulate_result import BlockchainSimulateResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainSimulateResult from a JSON string
blockchain_simulate_result_instance = BlockchainSimulateResult.from_json(json)
# print the JSON string representation of the object
print(BlockchainSimulateResult.to_json())

# convert the object into a dict
blockchain_simulate_result_dict = blockchain_simulate_result_instance.to_dict()
# create an instance of BlockchainSimulateResult from a dict
blockchain_simulate_result_from_dict = BlockchainSimulateResult.from_dict(blockchain_simulate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


