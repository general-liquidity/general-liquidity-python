# Page

A cursor-paginated page envelope. `data` holds the items; `next_cursor` names the last item so the next call resumes strictly after it (no overlap, no gap). Concrete `data` item types are given by the referencing operation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | 
**has_more** | **bool** | True when items remain after this page. | 
**next_cursor** | **str** | Token for the next page, or null when &#x60;has_more&#x60; is false. | 

## Example

```python
from general_liquidity.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


