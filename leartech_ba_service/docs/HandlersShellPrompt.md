# HandlersShellPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label is the human name for this prompt, if the cluster set one. Free text for a reader; Revision is what identifies it. | [optional] 
**prompt** | **str** | Prompt is the system prompt, or empty when this cluster sets none. | [optional] 
**revision** | **str** | Revision identifies this exact text.  A content hash, not a hand-set number. // proven-by: TestShellPrompt_RevisionIsDerivedFromTheContent A version someone has to remember to bump goes stale quietly, and two different prompts claiming one revision make every session recorded against it unreadable. Derived from the bytes, so it agrees with what was served.  proven-by: TestShellPrompt_RevisionIsDerivedFromTheContent proven-by: TestShellPrompt_DifferentPromptsNeverShareARevision | [optional] 
**source** | **str** | Source names where the value came from, for a client that has to tell an operator which prompt it is running. | [optional] 

## Example

```python
from leartech_ba_service.models.handlers_shell_prompt import HandlersShellPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of HandlersShellPrompt from a JSON string
handlers_shell_prompt_instance = HandlersShellPrompt.from_json(json)
# print the JSON string representation of the object
print(HandlersShellPrompt.to_json())

# convert the object into a dict
handlers_shell_prompt_dict = handlers_shell_prompt_instance.to_dict()
# create an instance of HandlersShellPrompt from a dict
handlers_shell_prompt_from_dict = HandlersShellPrompt.from_dict(handlers_shell_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


