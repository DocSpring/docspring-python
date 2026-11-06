# HtmlEngineOptions

How an HTML template's PDFs are printed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**PageFormat**](PageFormat.md) | The paper size. `Custom` uses `width` and `height`. | 
**width** | **str** | The page width for the `Custom` format, with a unit (`8.5in`, `210mm`), from 0.05in to 200in. | [optional] 
**height** | **str** | The page height for the `Custom` format, with a unit, from 0.05in to 200in. | [optional] 
**scale** | **float** | How much to scale the page, from 0.1 to 2, such as `0.8`. `1` prints it at its normal size. | 
**landscape** | **bool** | Print pages in landscape orientation. | 
**print_background** | **bool** | Print background colors and images. | 
**margin_top** | **str** | The top margin, with a unit, such as `1in` or `20mm`. The top and bottom margins together must be less than the page's height. | 
**margin_bottom** | **str** | The bottom margin, with a unit. | 
**margin_left** | **str** | The left margin, with a unit. The left and right margins together must be less than the page's width. | 
**margin_right** | **str** | The right margin, with a unit. | 

## Example

```python
from docspring.models.html_engine_options import HtmlEngineOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlEngineOptions from a JSON string
html_engine_options_instance = HtmlEngineOptions.from_json(json)
# print the JSON string representation of the object
print(HtmlEngineOptions.to_json())

# convert the object into a dict
html_engine_options_dict = html_engine_options_instance.to_dict()
# create an instance of HtmlEngineOptions from a dict
html_engine_options_from_dict = HtmlEngineOptions.from_dict(html_engine_options_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


