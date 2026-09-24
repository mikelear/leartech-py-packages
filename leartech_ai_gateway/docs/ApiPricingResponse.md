# ApiPricingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiPricingModel]**](ApiPricingModel.md) |  | [optional] 
**object** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**unpriced_count** | **int** | UnpricedCount is the same fact as the per-model flag, totalled, so a dashboard or a CLI can alert without walking the list. | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_pricing_response import ApiPricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPricingResponse from a JSON string
api_pricing_response_instance = ApiPricingResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPricingResponse.to_json())

# convert the object into a dict
api_pricing_response_dict = api_pricing_response_instance.to_dict()
# create an instance of ApiPricingResponse from a dict
api_pricing_response_from_dict = ApiPricingResponse.from_dict(api_pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


