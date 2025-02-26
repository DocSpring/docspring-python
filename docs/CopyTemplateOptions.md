# CopyTemplateOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_folder_id** | **str** |  | 

## Example

```python
from docspring.models.copy_template_options import CopyTemplateOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CopyTemplateOptions from a JSON string
copy_template_options_instance = CopyTemplateOptions.from_json(json)
# print the JSON string representation of the object
print(CopyTemplateOptions.to_json())

# convert the object into a dict
copy_template_options_dict = copy_template_options_instance.to_dict()
# create an instance of CopyTemplateOptions from a dict
copy_template_options_from_dict = CopyTemplateOptions.from_dict(copy_template_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


