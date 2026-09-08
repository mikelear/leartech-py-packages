# ApiUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[StoreUsageRow]**](StoreUsageRow.md) |  | [optional] 
**since** | **str** |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_usage_response import ApiUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsageResponse from a JSON string
api_usage_response_instance = ApiUsageResponse.from_json(json)
# print the JSON string representation of the object
print(ApiUsageResponse.to_json())

# convert the object into a dict
api_usage_response_dict = api_usage_response_instance.to_dict()
# create an instance of ApiUsageResponse from a dict
api_usage_response_from_dict = ApiUsageResponse.from_dict(api_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


