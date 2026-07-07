# TwoFactorSubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from leartech_auth_service.models.two_factor_submit_request import TwoFactorSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorSubmitRequest from a JSON string
two_factor_submit_request_instance = TwoFactorSubmitRequest.from_json(json)
# print the JSON string representation of the object
print(TwoFactorSubmitRequest.to_json())

# convert the object into a dict
two_factor_submit_request_dict = two_factor_submit_request_instance.to_dict()
# create an instance of TwoFactorSubmitRequest from a dict
two_factor_submit_request_from_dict = TwoFactorSubmitRequest.from_dict(two_factor_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


