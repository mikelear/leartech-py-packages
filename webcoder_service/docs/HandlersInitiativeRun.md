# HandlersInitiativeRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**HandlersInitiativeAssets**](HandlersInitiativeAssets.md) |  | [optional] 
**budget_iter** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**defer_reason** | **str** |  | [optional] 
**initiative** | **str** |  | [optional] 
**iteration** | **int** |  | [optional] 
**last_update** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 
**source_pr** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**target_pr** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 
**triggered_by** | **str** |  | [optional] 

## Example

```python
from webcoder_service.models.handlers_initiative_run import HandlersInitiativeRun

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersInitiativeRun from a JSON string
handlers_initiative_run_instance = HandlersInitiativeRun.from_json(json)
# print the JSON string representation of the object
print(HandlersInitiativeRun.to_json())

# convert the object into a dict
handlers_initiative_run_dict = handlers_initiative_run_instance.to_dict()
# create an instance of HandlersInitiativeRun from a dict
handlers_initiative_run_from_dict = HandlersInitiativeRun.from_dict(handlers_initiative_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


