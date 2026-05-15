# ExampleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Static demo message — replace with real service output. | 
**user_id** | **str** | Echoes back the validated user-id from the bearer token. | 

## Example

```python
from leartech_rust_service_template.models.example_response import ExampleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleResponse from a JSON string
example_response_instance = ExampleResponse.from_json(json)
# print the JSON string representation of the object
print(ExampleResponse.to_json())

# convert the object into a dict
example_response_dict = example_response_instance.to_dict()
# create an instance of ExampleResponse from a dict
example_response_from_dict = ExampleResponse.from_dict(example_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


