# TemplateDefaults

The default style of the template's fields. Each field can override it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typeface** | [**Typeface**](Typeface.md) | The font of text fields. | [optional] 
**font_size** | **float** | The font size in points, a whole number. | [optional] 
**character_spacing** | **float** | Extra space between characters, in points (0 to 50). | [optional] 
**color** | **str** | The text color, as 6 hex digits without `#`, such as `444444`. | [optional] 
**background_color** | **str** | The field's background color, as 6 hex digits. | [optional] 
**bold** | **bool** | Print text in bold. | [optional] 
**uppercase** | **bool** | Print text in capital letters. | [optional] 
**alignment** | [**TextAlignment**](TextAlignment.md) | How text is aligned in its field. `justify` lines up both edges of every line of multiline text except the last of each paragraph. | [optional] 
**opacity** | **float** | The opacity of the field's content, from 0 (invisible) to 1. | [optional] 
**date_format** | **str** | How date fields are printed, as a strftime format such as `%m/%d/%Y`. | [optional] 
**date_time_format** | **str** | How date-time fields are printed, as a strftime format such as `%m/%d/%Y %H:%M:%S`. | [optional] 
**check_color** | **str** | The color of check marks, as 6 hex digits. | [optional] 
**check_character** | [**CheckCharacter**](CheckCharacter.md) | The character that a ticked check box prints. | [optional] 
**check_background_color** | **str** | The check box's background color, as 6 hex digits. | [optional] 
**required_field_background_color** | **str** | The background color that highlights required fields on visual forms and signature request forms, as 6 hex digits. PDFs don't print it. | [optional] 
**true_text** | **str** | The text a boolean field prints for `true`. | [optional] 
**false_text** | **str** | The text a boolean field prints for `false`. | [optional] 
**shape_fill_color** | **str** | The fill color of shapes, as 6 hex digits. | [optional] 
**shape_border_color** | **str** | The border color of shapes, as 6 hex digits. | [optional] 
**shape_border_width** | **float** | The border width of shapes, in whole points (at least 1). | [optional] 

## Example

```python
from docspring.models.template_defaults import TemplateDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateDefaults from a JSON string
template_defaults_instance = TemplateDefaults.from_json(json)
# print the JSON string representation of the object
print(TemplateDefaults.to_json())

# convert the object into a dict
template_defaults_dict = template_defaults_instance.to_dict()
# create an instance of TemplateDefaults from a dict
template_defaults_from_dict = TemplateDefaults.from_dict(template_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


