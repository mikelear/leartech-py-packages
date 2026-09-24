# ApiPricingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosting** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**rates** | **Dict[str, int]** | Rates is micros per 1000 tokens, keyed by kind (input, output, cache_read, cache_write_5m, cache_write_1h). A kind ABSENT from this map has no rate on file; it is not zero. The distinction is the point of the endpoint — see Unpriced. | [optional] 
**unpriced** | **bool** | Unpriced reports that this model is callable and has NO input rate.  THIS IS THE FIELD THE ENDPOINT EXISTS FOR. A missing rate resolves to zero in the router&#39;s cost ranking, so an unpriced model reads as FREE and &#x60;auto&#x60; prefers it over every real supplier. Until now the only symptom was traffic silently moving. Reporting it as a boolean rather than as a zero in Rates keeps \&quot;costs nothing\&quot; and \&quot;nobody set a price\&quot; distinguishable, which is exactly the conflation that makes the defect invisible.  proven-by: TestPricing_AnUnpricedModelIsFlagged_NotReportedAsFree | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_pricing_model import ApiPricingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPricingModel from a JSON string
api_pricing_model_instance = ApiPricingModel.from_json(json)
# print the JSON string representation of the object
print(ApiPricingModel.to_json())

# convert the object into a dict
api_pricing_model_dict = api_pricing_model_instance.to_dict()
# create an instance of ApiPricingModel from a dict
api_pricing_model_from_dict = ApiPricingModel.from_dict(api_pricing_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


