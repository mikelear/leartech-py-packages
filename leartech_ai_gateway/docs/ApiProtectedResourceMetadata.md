# ApiProtectedResourceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | Audience is a DEVIATION and is named as one. RFC 9728 expects a client to pass &#x60;resource&#x60; (RFC 8707) and receive a correctly-audienced token. This estate issues tokens carrying a bare audience string instead (LEARTECH_AUTH_AUDIENCE, \&quot;leartech-ai-gateway\&quot;), and the verifier enforces that value. A client that knew only &#x60;resource&#x60; would request the wrong thing and be refused, so the value it actually needs is published rather than left to be guessed from a 401. | [optional] 
**authorization_servers** | **List[str]** | AuthorizationServers is where to get a token. One entry: a gateway answers to exactly one issuer, and LEARTECH_AUTH_ISSUER is the same value the verifier enforces, so this does not drift from what is accepted.  proven-by: TestProtectedResource_PublishesWhatTheVerifierEnforces | [optional] 
**bearer_methods_supported** | **List[str]** | BearerMethodsSupported: the gateway takes a bearer header, and virtual keys additionally arrive via x-api-key. Only the standard method is listed, because this document describes the OAUTH resource and a virtual key is not an OAuth credential. | [optional] 
**resource** | **str** | Resource identifies this deployment. Derived from the request rather than configured, because the gateway is reached on a different host per cluster and nothing tells it which -- there is no PUBLIC_URL, and adding one would be a second source for a fact the request already carries. | [optional] 
**scopes_supported** | **List[str]** | ScopesSupported is the published registry, not a hand-written list -- so a scope added to internal/authz appears here without anyone remembering to update a document. | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_protected_resource_metadata import ApiProtectedResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProtectedResourceMetadata from a JSON string
api_protected_resource_metadata_instance = ApiProtectedResourceMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiProtectedResourceMetadata.to_json())

# convert the object into a dict
api_protected_resource_metadata_dict = api_protected_resource_metadata_instance.to_dict()
# create an instance of ApiProtectedResourceMetadata from a dict
api_protected_resource_metadata_from_dict = ApiProtectedResourceMetadata.from_dict(api_protected_resource_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


