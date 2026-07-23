# Seal

A sealed hash+signature pair carried by every signed memory artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | 
**signature** | **str** |  | 

## Example

```python
from general_liquidity.models.seal import Seal

# TODO update the JSON string below
json = "{}"
# create an instance of Seal from a JSON string
seal_instance = Seal.from_json(json)
# print the JSON string representation of the object
print(Seal.to_json())

# convert the object into a dict
seal_dict = seal_instance.to_dict()
# create an instance of Seal from a dict
seal_from_dict = Seal.from_dict(seal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


