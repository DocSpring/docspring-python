# TemplatePageImages

A JPEG image of each page of a PDF template's PDF, at 140 DPI (a US Letter page is 1190 x 1540 pixels), to see the pages that fields are placed on. The template's `document.page_dimensions` gives each page's size in PDF points. Fields are placed in units where every page is 2480 wide: to place a field at a point on an image, multiply the point's pixel coordinates by 2480 and divide them by the image's `width`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | The template's ID. | 
**version** | **str** | The published version the images are of, such as `1.2.0`. Null for the draft. | 
**page_count** | **int** | How many pages the PDF has. | 
**pages** | [**List[PageImage]**](PageImage.md) | An image of each page, in order: `pages[0]` is page 1. Their `download_url`s expire, so get them again when you need them. | 

## Example

```python
from docspring.models.template_page_images import TemplatePageImages

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePageImages from a JSON string
template_page_images_instance = TemplatePageImages.from_json(json)
# print the JSON string representation of the object
print(TemplatePageImages.to_json())

# convert the object into a dict
template_page_images_dict = template_page_images_instance.to_dict()
# create an instance of TemplatePageImages from a dict
template_page_images_from_dict = TemplatePageImages.from_dict(template_page_images_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


