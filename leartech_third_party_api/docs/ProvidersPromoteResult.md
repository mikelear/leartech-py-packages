# ProvidersPromoteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_until_merged** | **bool** | PendingUntilMerged is true in the seed-store phase: the entry does not answer until the promote-PR merges, which is the whole point — a finding nobody reviewed must not become an integration contract. | [optional] 
**promote_pr** | **str** |  | [optional] 

## Example

```python
from leartech_third_party_api.models.providers_promote_result import ProvidersPromoteResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersPromoteResult from a JSON string
providers_promote_result_instance = ProvidersPromoteResult.from_json(json)
# print the JSON string representation of the object
print(ProvidersPromoteResult.to_json())

# convert the object into a dict
providers_promote_result_dict = providers_promote_result_instance.to_dict()
# create an instance of ProvidersPromoteResult from a dict
providers_promote_result_from_dict = ProvidersPromoteResult.from_dict(providers_promote_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


