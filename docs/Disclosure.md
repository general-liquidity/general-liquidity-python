# Disclosure

A signed self-description (identity + provenance). GL's disclosure format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Equals the ed25519 public key. | 
**document** | **object** |  | 
**signature** | **str** |  | 

## Example

```python
from general_liquidity.models.disclosure import Disclosure

# TODO update the JSON string below
json = "{}"
# create an instance of Disclosure from a JSON string
disclosure_instance = Disclosure.from_json(json)
# print the JSON string representation of the object
print(Disclosure.to_json())

# convert the object into a dict
disclosure_dict = disclosure_instance.to_dict()
# create an instance of Disclosure from a dict
disclosure_from_dict = Disclosure.from_dict(disclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


