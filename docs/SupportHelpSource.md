# SupportHelpSource

A documentation page an answer came from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The page's title. | 
**url** | **str** | The page's address. | 

## Example

```python
from docspring.models.support_help_source import SupportHelpSource

# TODO update the JSON string below
json = "{}"
# create an instance of SupportHelpSource from a JSON string
support_help_source_instance = SupportHelpSource.from_json(json)
# print the JSON string representation of the object
print(SupportHelpSource.to_json())

# convert the object into a dict
support_help_source_dict = support_help_source_instance.to_dict()
# create an instance of SupportHelpSource from a dict
support_help_source_from_dict = SupportHelpSource.from_dict(support_help_source_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


