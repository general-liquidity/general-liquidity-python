# CommerceLine

One requested line — a quantity of one merchant item. Carries no price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The merchant&#39;s own item identifier. | 
**quantity** | **int** | A positive integer count. Zero and fractional quantities are refused. | 

## Example

```python
from general_liquidity.models.commerce_line import CommerceLine

# TODO update the JSON string below
json = "{}"
# create an instance of CommerceLine from a JSON string
commerce_line_instance = CommerceLine.from_json(json)
# print the JSON string representation of the object
print(CommerceLine.to_json())

# convert the object into a dict
commerce_line_dict = commerce_line_instance.to_dict()
# create an instance of CommerceLine from a dict
commerce_line_from_dict = CommerceLine.from_dict(commerce_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


