# InternalHandlersExampleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from leartech_plan_conformance_consumer.models.internal_handlers_example_response import InternalHandlersExampleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlersExampleResponse from a JSON string
internal_handlers_example_response_instance = InternalHandlersExampleResponse.from_json(json)
# print the JSON string representation of the object
print(InternalHandlersExampleResponse.to_json())

# convert the object into a dict
internal_handlers_example_response_dict = internal_handlers_example_response_instance.to_dict()
# create an instance of InternalHandlersExampleResponse from a dict
internal_handlers_example_response_from_dict = InternalHandlersExampleResponse.from_dict(internal_handlers_example_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


