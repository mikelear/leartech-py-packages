# ApiTransformSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint** | **object** | Checkpoint is the rewritten session, ready for the shell to save to a new resume slot and continue on TargetModel. It re-chains onto the source (prev_hash &#x3D; source hash), exactly as compact does, so the switch is one recorded link rather than a hidden edit. | [optional] 
**object** | **str** | \&quot;session.transform\&quot; | [optional] 
**report** | [**ApiTransformReport**](ApiTransformReport.md) | Report names every change, so the switch is auditable. | [optional] 
**target_model** | **str** | TargetModel echoes what the session was transformed FOR. | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_transform_session_response import ApiTransformSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTransformSessionResponse from a JSON string
api_transform_session_response_instance = ApiTransformSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ApiTransformSessionResponse.to_json())

# convert the object into a dict
api_transform_session_response_dict = api_transform_session_response_instance.to_dict()
# create an instance of ApiTransformSessionResponse from a dict
api_transform_session_response_from_dict = ApiTransformSessionResponse.from_dict(api_transform_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


