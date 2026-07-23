# AssembleRequestRecall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_at** | **datetime** |  | 
**tx_at** | **datetime** |  | 

## Example

```python
from general_liquidity.models.assemble_request_recall import AssembleRequestRecall

# TODO update the JSON string below
json = "{}"
# create an instance of AssembleRequestRecall from a JSON string
assemble_request_recall_instance = AssembleRequestRecall.from_json(json)
# print the JSON string representation of the object
print(AssembleRequestRecall.to_json())

# convert the object into a dict
assemble_request_recall_dict = assemble_request_recall_instance.to_dict()
# create an instance of AssembleRequestRecall from a dict
assemble_request_recall_from_dict = AssembleRequestRecall.from_dict(assemble_request_recall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


