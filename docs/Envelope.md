# Envelope

The layered signed delegation wrapping an Intent — identity + mandate + provenance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | **str** | Caller agent id (signed disclosure / ERC-8004, CAIP-addressed). | 
**mandate_id** | **str** |  | 
**grant** | [**Grant**](Grant.md) |  | 
**signature** | **str** |  | 

## Example

```python
from general_liquidity.models.envelope import Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of Envelope from a JSON string
envelope_instance = Envelope.from_json(json)
# print the JSON string representation of the object
print(Envelope.to_json())

# convert the object into a dict
envelope_dict = envelope_instance.to_dict()
# create an instance of Envelope from a dict
envelope_from_dict = Envelope.from_dict(envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


