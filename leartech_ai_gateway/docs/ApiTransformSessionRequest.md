# ApiTransformSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint** | **object** | Checkpoint is the saved session, exactly as the shell wrote it — the agentloop.Checkpoint shape (version, turn, prev_hash, hash, messages). | 
**reply_headroom_tokens** | **int** | ReplyHeadroomTokens is how much of the target window to leave free for the next reply. OPTIONAL; a sensible default is applied. Mirrors the shell&#39;s compact headroom so the two paths size the same way. | [optional] 
**source_model** | **str** | SourceModel is the model the session was recorded against, when the caller knows it. OPTIONAL: it is used only to describe the switch in the bridge note and the response; the transform does not depend on it, since the rewrite is driven by the TARGET model&#39;s needs. | [optional] 
**target_model** | **str** | TargetModel is the logical model the session should be resumed on. It is resolved against the caller&#39;s catalogue, so an unknown or disallowed model is refused the same way a chat call would be. | 

## Example

```python
from leartech_ai_gateway.models.api_transform_session_request import ApiTransformSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTransformSessionRequest from a JSON string
api_transform_session_request_instance = ApiTransformSessionRequest.from_json(json)
# print the JSON string representation of the object
print(ApiTransformSessionRequest.to_json())

# convert the object into a dict
api_transform_session_request_dict = api_transform_session_request_instance.to_dict()
# create an instance of ApiTransformSessionRequest from a dict
api_transform_session_request_from_dict = ApiTransformSessionRequest.from_dict(api_transform_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


