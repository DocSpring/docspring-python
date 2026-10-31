# FieldOverride

Changes to one field's settings for this submission only. Settings left out keep the template's.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static** | **bool** | Print the field's `default` (a fixed value, or a formula for a number field) on the PDF instead of a value from `data`. | [optional] 
**editable** | **bool** | Keep this field fillable in the PDF instead of flattening it to text. The submission's `editable` overrides it. | [optional] 
**default** | **str** | The value used when `data` has none for the field. | [optional] 
**title** | **str** | The field's label on the signing form. | [optional] 
**required** | **bool** | Whether `data` must have a value for the field. | [optional] 
**option_list** | **str** | The values the field can take, separated by commas, such as `Yes,No`. Null allows any value. | [optional] 
**combined_field_names** | **str** | The names of the fields a combined field joins, separated by commas. | [optional] 
**combined_field_type** | [**CombinedFieldType**](CombinedFieldType.md) | How a combined field joins its fields' values. | [optional] 
**combined_field_separator** | **str** | The text between the values of a combined field, such as `, `. | [optional] 
**combined_field_format** | **str** | The text a combined field prints, with `$0`, `$1` and so on for its fields' values, such as `$0, $1`. | [optional] 
**integer** | **bool** | Whether a number field takes only whole numbers. | [optional] 
**include_time** | **bool** | Whether a date field takes a date and time (RFC 3339) rather than a date (YYYY-MM-DD). | [optional] 
**signature_allow_draw** | **bool** | Let the person draw their signature or initials on the signing form. | [optional] 
**signature_allow_type** | **bool** | Let the person type their signature or initials on the signing form. | [optional] 
**barcode_symbology** | [**BarcodeSymbology**](BarcodeSymbology.md) | The kind of barcode a field with display_type `barcode` prints. | [optional] 
**hidden** | **bool** | Leave the field off the PDF. Its value is still in the data, and combined fields can use it. | [optional] 
**x** | **float** | The distance from the left edge of the page, in the template editor's page units. | [optional] 
**y** | **float** | The distance from the top of the page, in the template editor's page units. | [optional] 
**width** | **float** | The field's width, in the template editor's page units. | [optional] 
**height** | **float** | The field's height, in the template editor's page units. | [optional] 
**rotation** | **float** | The field's rotation in degrees, clockwise. | [optional] 
**display_type** | [**FieldDisplayType**](FieldDisplayType.md) | How the field's value is drawn on the PDF. | [optional] 
**opacity** | **float** | The field's opacity, from 0 (invisible) to 1 (solid). | [optional] 
**date_time_format** | **str** | How a date field's value is printed, as a strftime format such as `%m/%d/%Y`. Null uses the template's date format. | [optional] 
**typeface** | [**Typeface**](Typeface.md) | The font of the field's text. Null uses the template's default. | [optional] 
**font_size** | **int** | The font size in points, a whole number. Null uses the template's default. | [optional] 
**character_spacing** | **float** | Extra space between characters, in points (0 to 50). | [optional] 
**bold** | **bool** | Print the text in bold. | [optional] 
**uppercase** | **bool** | Print the text in capitals. | [optional] 
**strikethrough** | **bool** | Strike through the text. | [optional] 
**keep_leading_spaces** | **bool** | Keep the spaces at the start of the text and of each line, so you can line text up with spaces. | [optional] 
**overflow** | [**TextOverflow**](TextOverflow.md) | What happens to text that doesn't fit in the field. | [optional] 
**multiline** | **bool** | Wrap the text over several lines when it doesn't fit on one. | [optional] 
**multiline_lines** | **int** | The number of lines in a multiline field, for a PDF with ruled lines. Null for no fixed number of lines. | [optional] 
**max_length** | **int** | The most characters the field takes. Null for no limit. | [optional] 
**color** | **str** | The text color, as 6 hex digits without `#`, such as `444444`. Null uses the template's default. | [optional] 
**background_color** | **str** | The field's background color, as 6 hex digits without `#`. Null for none. | [optional] 
**alignment** | [**TextAlignment**](TextAlignment.md) | How text is aligned in its field. `justify` lines up both edges of every line of multiline text except the last of each paragraph. | [optional] 
**v_alignment** | [**TextVerticalAlignment**](TextVerticalAlignment.md) | How text is aligned vertically in its field. | [optional] 
**comb** | **bool** | Print one character in each of the field's equally spaced boxes (combs). | [optional] 
**comb_number_of_cells** | **int** | The number of boxes in a comb field. | [optional] 
**comb_value_offset** | **int** | The character of the value that the first box starts from, for a value split over several comb fields (such as the parts of a Social Security number). | [optional] 
**shape_type** | [**ShapeType**](ShapeType.md) | The shape a field with display_type `shape` draws. | [optional] 
**shape_sides** | **int** | The number of sides of a `polygon` shape. | [optional] 
**shape_border_width** | **int** | The width of a shape's border, in points, a whole number. | [optional] 
**shape_border_color** | **str** | The color of a shape's border, as 6 hex digits without `#`. | [optional] 
**shape_fill_color** | **str** | The color a shape is filled with, as 6 hex digits without `#`. Null for no fill. | [optional] 
**check_character** | [**CheckCharacter**](CheckCharacter.md) | The character that a ticked check box prints. | [optional] 
**check_color** | **str** | The color of the check mark, as 6 hex digits without `#`. Null uses the template's default. | [optional] 
**qrcode_color** | **str** | The color of a QR code, as 6 hex digits without `#`. Null for black. | [optional] 
**true_text** | **str** | What a boolean field with display_type `text` prints for `true`. | [optional] 
**false_text** | **str** | What a boolean field with display_type `text` prints for `false`. | [optional] 
**condition** | **str** | The value a check mark or shape is drawn for: it's drawn when the field's value matches, as `string_condition_type` or `number_condition_type` says. | [optional] 
**string_condition_type** | [**StringConditionType**](StringConditionType.md) | How a string field's value is compared with `condition`. | [optional] 
**number_condition_type** | [**NumberConditionType**](NumberConditionType.md) | How a number field's value is compared with `condition`, or with `number_condition_range_min` and `number_condition_range_max` for `range`. | [optional] 
**number_condition_range_min** | **float** | The lower end of a `range` condition. | [optional] 
**number_condition_range_max** | **float** | The upper end of a `range` condition. | [optional] 
**number_condition_range_exclusive_min** | **bool** | Leave the lower end itself out of a `range` condition. | [optional] 
**number_condition_range_exclusive_max** | **bool** | Leave the upper end itself out of a `range` condition. | [optional] 
**invert_boolean_condition** | **bool** | Draw a boolean field's check mark or shape for `false` instead of `true`. | [optional] 
**decimal_places** | **int** | The number of decimal places a number field prints. Null prints the value as it was sent. | [optional] 
**image_scale_type** | [**ImageScaleType**](ImageScaleType.md) | How an image is resized to its field. | [optional] 
**image_gravity** | [**ImageGravity**](ImageGravity.md) | Where an image sits in its field when it doesn't fill it, or which part is kept when it's cropped. | [optional] 

## Example

```python
from docspring.models.field_override import FieldOverride

# TODO update the JSON string below
json = "{}"
# create an instance of FieldOverride from a JSON string
field_override_instance = FieldOverride.from_json(json)
# print the JSON string representation of the object
print(FieldOverride.to_json())

# convert the object into a dict
field_override_dict = field_override_instance.to_dict()
# create an instance of FieldOverride from a dict
field_override_from_dict = FieldOverride.from_dict(field_override_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


