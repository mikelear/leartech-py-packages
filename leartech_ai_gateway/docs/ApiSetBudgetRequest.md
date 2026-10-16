# ApiSetBudgetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_micros** | **int** | BudgetMicros is the new ABSOLUTE monthly spend cap in micros (1e6 &#x3D; $1). Required and positive: an absent or zero cap would be a different operation (revoke / disable), not a budget set. | 

## Example

```python
from leartech_ai_gateway.models.api_set_budget_request import ApiSetBudgetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetBudgetRequest from a JSON string
api_set_budget_request_instance = ApiSetBudgetRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSetBudgetRequest.to_json())

# convert the object into a dict
api_set_budget_request_dict = api_set_budget_request_instance.to_dict()
# create an instance of ApiSetBudgetRequest from a dict
api_set_budget_request_from_dict = ApiSetBudgetRequest.from_dict(api_set_budget_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


