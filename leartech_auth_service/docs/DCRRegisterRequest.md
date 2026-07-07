# DCRRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** |  | [optional] 
**contacts** | **List[str]** |  | [optional] 
**grant_types** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**response_types** | **List[str]** |  | [optional] 
**scope** | **str** |  | [optional] 
**software_id** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 

## Example

```python
from leartech_auth_service.models.dcr_register_request import DCRRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DCRRegisterRequest from a JSON string
dcr_register_request_instance = DCRRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(DCRRegisterRequest.to_json())

# convert the object into a dict
dcr_register_request_dict = dcr_register_request_instance.to_dict()
# create an instance of DCRRegisterRequest from a dict
dcr_register_request_from_dict = DCRRegisterRequest.from_dict(dcr_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


