# BlockchainPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[object]** | Args are the constructor arguments, in ABI order. | [optional] 
**bytecode** | **str** | Bytecode is the contract&#39;s creation code, 0x-hex. When empty the plan reports the finding and does not estimate gas — deploying a transaction with no init code is a caller error we surface, not one we paper over. | [optional] 
**chain** | **str** | Chain is a label for the deployment row; the chainId comes from the node the service is wired to. | [optional] 
**contract** | **str** | Contract is the catalog name whose ABI defines the constructor — \&quot;MockOracle\&quot; / \&quot;MockConsumer\&quot; today. | 
**var_from** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_plan_request import BlockchainPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainPlanRequest from a JSON string
blockchain_plan_request_instance = BlockchainPlanRequest.from_json(json)
# print the JSON string representation of the object
print(BlockchainPlanRequest.to_json())

# convert the object into a dict
blockchain_plan_request_dict = blockchain_plan_request_instance.to_dict()
# create an instance of BlockchainPlanRequest from a dict
blockchain_plan_request_from_dict = BlockchainPlanRequest.from_dict(blockchain_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


