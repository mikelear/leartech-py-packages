# TwoFactorEnableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qr_code_url** | **str** |  | [optional] 
**recovery_codes** | **List[str]** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.two_factor_enable_response import TwoFactorEnableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorEnableResponse from a JSON string
two_factor_enable_response_instance = TwoFactorEnableResponse.from_json(json)
# print the JSON string representation of the object
print(TwoFactorEnableResponse.to_json())

# convert the object into a dict
two_factor_enable_response_dict = two_factor_enable_response_instance.to_dict()
# create an instance of TwoFactorEnableResponse from a dict
two_factor_enable_response_from_dict = TwoFactorEnableResponse.from_dict(two_factor_enable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


