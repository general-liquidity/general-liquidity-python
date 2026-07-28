# KeyRotationStatement

One signed hop of a key-rotation chain: the old key signs the move to the new key, so an identity survives a key change (an agentId IS its public key). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_from** | **str** | agentId (public key hex) being rotated away from. | 
**to** | **str** | agentId (public key hex) being rotated to. | 
**rotated_at** | **datetime** |  | 
**signature** | **str** | Old key&#39;s signature over {type, from, to, rotatedAt} (hex). | 

## Example

```python
from general_liquidity.models.key_rotation_statement import KeyRotationStatement

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRotationStatement from a JSON string
key_rotation_statement_instance = KeyRotationStatement.from_json(json)
# print the JSON string representation of the object
print(KeyRotationStatement.to_json())

# convert the object into a dict
key_rotation_statement_dict = key_rotation_statement_instance.to_dict()
# create an instance of KeyRotationStatement from a dict
key_rotation_statement_from_dict = KeyRotationStatement.from_dict(key_rotation_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


