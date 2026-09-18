# ApiUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_tokens** | **int** |  | [optional] 
**leartech_cache** | [**ApiLeartechCache**](ApiLeartechCache.md) |  | [optional] 
**prompt_tokens** | **int** |  | [optional] 
**prompt_tokens_details** | [**ApiPromptTokensDetails**](ApiPromptTokensDetails.md) | ONE CONVENTION IN THIS OBJECT: every detail field below is a SUBSET of PromptTokens, which is every prompt token processed. Reads and writes are disjoint subsets — a prefix is either served from cache or written to it, not both in one request.  Subset rather than additive, and the reason is a client we did not write. A naive OpenAI client reads prompt_tokens, ignores every detail field and multiplies by the input rate: under subset that OVER-estimates, because the cached portion actually bills at a fraction; under additive it UNDER-estimates by two orders of magnitude, because the written tokens carry a premium and are invisible. Erring safe for the clients we control least follows the same principle as absence-resolving-to-the-input-rate.  It also keeps total_tokens honest: because PromptTokens is already the whole, total &#x3D; prompt + completion is simultaneously OpenAI-pure and reconcilable against the cost on the same response. Under an additive extension those two are in conflict and something has to give.  proven-by: TestUsageResponse_IsLosslessAcrossTheConventionFlip proven-by: TestUsageResponse_TotalTokensStaysOpenAIPure | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_usage import ApiUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsage from a JSON string
api_usage_instance = ApiUsage.from_json(json)
# print the JSON string representation of the object
print(ApiUsage.to_json())

# convert the object into a dict
api_usage_dict = api_usage_instance.to_dict()
# create an instance of ApiUsage from a dict
api_usage_from_dict = ApiUsage.from_dict(api_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


