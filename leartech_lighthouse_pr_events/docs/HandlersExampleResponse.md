# HandlersExampleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from leartech_lighthouse_pr_events.models.handlers_example_response import HandlersExampleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersExampleResponse from a JSON string
handlers_example_response_instance = HandlersExampleResponse.from_json(json)
# print the JSON string representation of the object
print(HandlersExampleResponse.to_json())

# convert the object into a dict
handlers_example_response_dict = handlers_example_response_instance.to_dict()
# create an instance of HandlersExampleResponse from a dict
handlers_example_response_from_dict = HandlersExampleResponse.from_dict(handlers_example_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


