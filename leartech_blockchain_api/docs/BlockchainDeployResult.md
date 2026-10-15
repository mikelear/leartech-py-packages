# BlockchainDeployResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** |  | [optional] 
**chain_id** | **int** |  | [optional] 
**contract** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**transaction** | [**BlockchainSubmitResult**](BlockchainSubmitResult.md) |  | [optional] 
**warning** | **str** | Warning carries a non-fatal post-broadcast problem (the deployment row did not land) so the 202 body can hold BOTH the hash the caller needs and the thing that went wrong around it. | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_deploy_result import BlockchainDeployResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDeployResult from a JSON string
blockchain_deploy_result_instance = BlockchainDeployResult.from_json(json)
# print the JSON string representation of the object
print(BlockchainDeployResult.to_json())

# convert the object into a dict
blockchain_deploy_result_dict = blockchain_deploy_result_instance.to_dict()
# create an instance of BlockchainDeployResult from a dict
blockchain_deploy_result_from_dict = BlockchainDeployResult.from_dict(blockchain_deploy_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


