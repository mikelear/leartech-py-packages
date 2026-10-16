# CapabilitiesPromoteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_until_merged** | **bool** |  | [optional] 
**promote_pr** | **str** |  | [optional] 

## Example

```python
from leartech_platform_capabilities_api.models.capabilities_promote_result import CapabilitiesPromoteResult

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesPromoteResult from a JSON string
capabilities_promote_result_instance = CapabilitiesPromoteResult.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesPromoteResult.to_json())

# convert the object into a dict
capabilities_promote_result_dict = capabilities_promote_result_instance.to_dict()
# create an instance of CapabilitiesPromoteResult from a dict
capabilities_promote_result_from_dict = CapabilitiesPromoteResult.from_dict(capabilities_promote_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


