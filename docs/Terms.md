# Terms

The six irreducible fields — explicit on every Intent and Receipt, never silently defaulted. This is what the Gate reasons over. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reversibility** | [**Reversibility**](Reversibility.md) |  | 
**finality** | [**Finality**](Finality.md) |  | 
**credential** | **str** | Authorization model id, e.g. \&quot;eip3009\&quot; | \&quot;vc-mandate\&quot; | \&quot;http-sig\&quot;. | 
**rail** | [**RailId**](RailId.md) |  | 
**capital_source** | [**CapitalSource**](CapitalSource.md) |  | 
**presence** | [**Presence**](Presence.md) |  | 

## Example

```python
from general_liquidity.models.terms import Terms

# TODO update the JSON string below
json = "{}"
# create an instance of Terms from a JSON string
terms_instance = Terms.from_json(json)
# print the JSON string representation of the object
print(Terms.to_json())

# convert the object into a dict
terms_dict = terms_instance.to_dict()
# create an instance of Terms from a dict
terms_from_dict = Terms.from_dict(terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


