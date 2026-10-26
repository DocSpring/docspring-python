# PredefinedField

A field name that people using the embedded template editor can choose from, with the data type and settings a field gets when it's given that name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The field's name, the key of its value in submission data. A `/` nests the key in objects and arrays (`customer/email`, `signers/0/name`). | 
**display_name** | **str** | The name the template editor shows instead of `name`, where a `/` puts it in a folder, such as `Defendant/Name`. Null shows `name`. Two names can't share a display name. | [optional] 
**title** | **str** | The Title setting a field gets when it's given this name. Null leaves the field's title as it is. | [optional] 
**type** | [**FieldType**](FieldType.md) | The data type a field gets when it's given this name, as a field's `type`. | 
**option_list** | **str** | String fields only: the values allowed, separated by commas, such as `Yes,No`. Null allows any value. | [optional] 
**required_in_template** | **bool** | Whether the template must have a field with this name. The embedded editor shows the names that are missing, and with `disableDoneButtonIfPredefinedFieldsMissing` keeps its Done button disabled until the template has them. Default false. | [optional] 
**field_required** | **bool** | The Required setting a field gets when it's given this name. Default true. | [optional] 

## Example

```python
from docspring.models.predefined_field import PredefinedField

# TODO update the JSON string below
json = "{}"
# create an instance of PredefinedField from a JSON string
predefined_field_instance = PredefinedField.from_json(json)
# print the JSON string representation of the object
print(PredefinedField.to_json())

# convert the object into a dict
predefined_field_dict = predefined_field_instance.to_dict()
# create an instance of PredefinedField from a dict
predefined_field_from_dict = PredefinedField.from_dict(predefined_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


