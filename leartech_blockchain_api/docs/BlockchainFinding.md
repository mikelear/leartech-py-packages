# BlockchainFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | \&quot;error\&quot; | \&quot;warning\&quot; | \&quot;info\&quot; | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from leartech_blockchain_api.models.blockchain_finding import BlockchainFinding

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainFinding from a JSON string
blockchain_finding_instance = BlockchainFinding.from_json(json)
# print the JSON string representation of the object
print(BlockchainFinding.to_json())

# convert the object into a dict
blockchain_finding_dict = blockchain_finding_instance.to_dict()
# create an instance of BlockchainFinding from a dict
blockchain_finding_from_dict = BlockchainFinding.from_dict(blockchain_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


