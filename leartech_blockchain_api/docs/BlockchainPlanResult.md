# BlockchainPlanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abi** | **Dict[str, object]** |  | [optional] 
**args** | **List[object]** |  | [optional] 
**bytecode** | **str** |  | [optional] 
**calldata** | **str** |  | [optional] 
**chain** | **str** |  | [optional] 
**chain_id** | **int** |  | [optional] 
**constructor** | **str** |  | [optional] 
**contract** | **str** |  | [optional] 
**dry_run** | **bool** |  | [optional] 
**encoded_args** | **str** |  | [optional] 
**findings** | [**List[BlockchainFinding]**](BlockchainFinding.md) | Findings carries the plan&#39;s validation results, serialised with no omitempty so a plan with nothing to flag still answers \&quot;findings\&quot;: []. A reviewer diffing two plans reads the field&#39;s absence as \&quot;the service predates findings\&quot;, distinct from an empty list meaning \&quot;nothing flagged\&quot;. proven-by: TestPlan_FindingsIsAlwaysAnArray | [optional] 
**gas_estimate** | **int** |  | [optional] 
**gas_source** | **str** |  | [optional] 
**signer** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_plan_result import BlockchainPlanResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainPlanResult from a JSON string
blockchain_plan_result_instance = BlockchainPlanResult.from_json(json)
# print the JSON string representation of the object
print(BlockchainPlanResult.to_json())

# convert the object into a dict
blockchain_plan_result_dict = blockchain_plan_result_instance.to_dict()
# create an instance of BlockchainPlanResult from a dict
blockchain_plan_result_from_dict = BlockchainPlanResult.from_dict(blockchain_plan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


