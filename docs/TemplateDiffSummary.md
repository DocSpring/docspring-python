# TemplateDiffSummary

How many changes of each kind a template diff has.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields_added** | **int** | How many fields were added. | 
**fields_removed** | **int** | How many fields were removed. | 
**fields_changed** | **int** | How many fields have changed settings. | 
**fields_reordered** | **int** | How many fields moved in the template's field order. | 
**settings_changed** | **int** | How many of the template's settings changed. | 
**total_changes** | **int** | All the changes, counting a new document as one. Zero when the versions are the same. | 

## Example

```python
from docspring.models.template_diff_summary import TemplateDiffSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDiffSummary from a JSON string
template_diff_summary_instance = TemplateDiffSummary.from_json(json)
# print the JSON string representation of the object
print(TemplateDiffSummary.to_json())

# convert the object into a dict
template_diff_summary_dict = template_diff_summary_instance.to_dict()
# create an instance of TemplateDiffSummary from a dict
template_diff_summary_from_dict = TemplateDiffSummary.from_dict(template_diff_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


