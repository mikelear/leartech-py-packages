# HandlersCreateInitiativeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiative_yaml** | **str** | InitiativeYaml is the full YAML body of the initiative. Mutually exclusive with Template/Params. | [optional] 
**params** | **Dict[str, object]** | Params populate the template&#39;s variables when Template is set. | [optional] 
**template** | **str** | Template is the name of an initiatives/_templates/&lt;name&gt;.yaml template to instantiate. Mutually exclusive with InitiativeYaml. | [optional] 

## Example

```python
from webcoder_service.models.handlers_create_initiative_request import HandlersCreateInitiativeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersCreateInitiativeRequest from a JSON string
handlers_create_initiative_request_instance = HandlersCreateInitiativeRequest.from_json(json)
# print the JSON string representation of the object
print(HandlersCreateInitiativeRequest.to_json())

# convert the object into a dict
handlers_create_initiative_request_dict = handlers_create_initiative_request_instance.to_dict()
# create an instance of HandlersCreateInitiativeRequest from a dict
handlers_create_initiative_request_from_dict = HandlersCreateInitiativeRequest.from_dict(handlers_create_initiative_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


