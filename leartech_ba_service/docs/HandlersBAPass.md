# HandlersBAPass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answered** | **int** | questions closed this pass (0 or 1 — one per pass) | [optional] 
**at** | **str** |  | [optional] 
**error** | **str** | the failure, verbatim, when the pass failed | [optional] 
**exhausted** | **bool** | R1 tripped; nothing picked up | [optional] 
**pr** | **str** | the finding PR, when one was filed | [optional] 

## Example

```python
from leartech_ba_service.models.handlers_ba_pass import HandlersBAPass

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersBAPass from a JSON string
handlers_ba_pass_instance = HandlersBAPass.from_json(json)
# print the JSON string representation of the object
print(HandlersBAPass.to_json())

# convert the object into a dict
handlers_ba_pass_dict = handlers_ba_pass_instance.to_dict()
# create an instance of HandlersBAPass from a dict
handlers_ba_pass_from_dict = HandlersBAPass.from_dict(handlers_ba_pass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


