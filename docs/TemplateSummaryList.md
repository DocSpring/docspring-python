# TemplateSummaryList

A page of templates (drafts), newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TemplateSummary]**](TemplateSummary.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.template_summary_list import TemplateSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSummaryList from a JSON string
template_summary_list_instance = TemplateSummaryList.from_json(json)
# print the JSON string representation of the object
print(TemplateSummaryList.to_json())

# convert the object into a dict
template_summary_list_dict = template_summary_list_instance.to_dict()
# create an instance of TemplateSummaryList from a dict
template_summary_list_from_dict = TemplateSummaryList.from_dict(template_summary_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


