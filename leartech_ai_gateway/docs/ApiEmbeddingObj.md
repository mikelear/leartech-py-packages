# ApiEmbeddingObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | **List[float]** |  | [optional] 
**index** | **int** |  | [optional] 
**object** | **str** | \&quot;embedding\&quot; | [optional] 

## Example

```python
from leartech_ai_gateway.models.api_embedding_obj import ApiEmbeddingObj

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEmbeddingObj from a JSON string
api_embedding_obj_instance = ApiEmbeddingObj.from_json(json)
# print the JSON string representation of the object
print(ApiEmbeddingObj.to_json())

# convert the object into a dict
api_embedding_obj_dict = api_embedding_obj_instance.to_dict()
# create an instance of ApiEmbeddingObj from a dict
api_embedding_obj_from_dict = ApiEmbeddingObj.from_dict(api_embedding_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


