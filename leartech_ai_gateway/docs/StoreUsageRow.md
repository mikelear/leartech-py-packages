# StoreUsageRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls** | **int** |  | [optional] 
**completion_tokens** | **int** |  | [optional] 
**cost_micros** | **int** |  | [optional] 
**keyid** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**prompt_tokens** | **int** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.store_usage_row import StoreUsageRow

# TODO update the JSON string below
json = "{}"
# create an instance of StoreUsageRow from a JSON string
store_usage_row_instance = StoreUsageRow.from_json(json)
# print the JSON string representation of the object
print(StoreUsageRow.to_json())

# convert the object into a dict
store_usage_row_dict = store_usage_row_instance.to_dict()
# create an instance of StoreUsageRow from a dict
store_usage_row_from_dict = StoreUsageRow.from_dict(store_usage_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


