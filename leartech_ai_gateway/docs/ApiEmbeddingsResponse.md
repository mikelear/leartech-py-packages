# ApiEmbeddingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiEmbeddingObj]**](ApiEmbeddingObj.md) |  | [optional] 
**model** | **str** |  | [optional] 
**object** | **str** | \&quot;list\&quot; | [optional] 
**usage** | [**ApiUsage**](ApiUsage.md) |  | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_embeddings_response import ApiEmbeddingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEmbeddingsResponse from a JSON string
api_embeddings_response_instance = ApiEmbeddingsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiEmbeddingsResponse.to_json())

# convert the object into a dict
api_embeddings_response_dict = api_embeddings_response_instance.to_dict()
# create an instance of ApiEmbeddingsResponse from a dict
api_embeddings_response_from_dict = ApiEmbeddingsResponse.from_dict(api_embeddings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


