# PendingSettlement

An RFC 7807 problem (type `clearing.pending`) returned when an optional PENDING clearing band holds a bound spend: it was gated and authorized, but the obligation's admissibility floor is not yet met and the deadline has not passed, so the value is HELD rather than settled or refused. Retry once admissible evidence exists (the hold auto-releases to a `Receipt`); the hold refuses once the deadline passes. Only present on a stack that wired the clearing band's PENDING state. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**obligation_id** | **str** | The obligation the spend is conditional on. | 
**state** | **str** |  | 
**awaiting** | [**EvidenceClass**](EvidenceClass.md) | The admissibility class still awaited before the spend can settle. | 
**achieved_class** | [**EvidenceClass**](EvidenceClass.md) | The strongest class the admitted evidence has reached so far. | [optional] 

## Example

```python
from general_liquidity.models.pending_settlement import PendingSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of PendingSettlement from a JSON string
pending_settlement_instance = PendingSettlement.from_json(json)
# print the JSON string representation of the object
print(PendingSettlement.to_json())

# convert the object into a dict
pending_settlement_dict = pending_settlement_instance.to_dict()
# create an instance of PendingSettlement from a dict
pending_settlement_from_dict = PendingSettlement.from_dict(pending_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


