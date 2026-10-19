# ApiTransformReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_tokens** | **int** |  | [optional] 
**before_tokens** | **int** | BeforeTokens and AfterTokens are the gateway&#39;s own estimate (chars/4) either side, the same arithmetic the context-window gate enforces with. | [optional] 
**bridge_added** | **bool** | BridgeAdded is whether a system \&quot;you are continuing a conversation begun with another model\&quot; note was inserted, so the new model understands it is resuming rather than starting. | [optional] 
**compacted** | **int** | Compacted is how many tool results were elided to fit the target window, 0 when the session already fit. | [optional] 
**fit** | **bool** | Fit is whether the session reached the target window with reply headroom. proven-by: TestTransformForModel_SaysWhenItCannotFit | [optional] 
**notes** | **List[str]** | Notes are human-readable lines describing each change and its reason. | [optional] 
**target_max_ctx** | **int** | TargetMaxCtx is the target model&#39;s advertised context window, the ceiling the transform fit the session under. | [optional] 
**tool_ids_rekeyed** | **int** | ToolIDsRekeyed is how many tool-call ids were rewritten to a neutral format so the call/result pairing survives a cross-provider switch. | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_transform_report import ApiTransformReport

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTransformReport from a JSON string
api_transform_report_instance = ApiTransformReport.from_json(json)
# print the JSON string representation of the object
print(ApiTransformReport.to_json())

# convert the object into a dict
api_transform_report_dict = api_transform_report_instance.to_dict()
# create an instance of ApiTransformReport from a dict
api_transform_report_from_dict = ApiTransformReport.from_dict(api_transform_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


