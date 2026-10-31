# PageImage

An image of one page of a PDF, a PNG of a submission's page or a JPEG of a template's.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number, from 1. | 
**width** | **int** | The image's width in pixels. | 
**height** | **int** | The image's height in pixels. | 
**download_url** | **str** | A temporary link to download the image. A submission's is null when your account turns off download links for submissions. | 
**permanent_url** | **str** | A link to download a submission's image that doesn't expire: it redirects to a new temporary link. It needs your API token or a signed-in session, except for a submission of a template that makes its submissions public. Null for a template's page images. | 
**filename** | **str** | The image's file name, such as `sub_123_page_1.png`. | 
**content_type** | **str** | The image's media type, `image/png` for a submission's pages or `image/jpeg` for a template's. | 
**size** | **int** | The image's size in bytes. | 
**sha256** | **str** | The SHA-256 hash of the image. Null for a template's page images. | 

## Example

```python
from docspring.models.page_image import PageImage

# TODO update the JSON string below
json = "{}"
# create an instance of PageImage from a JSON string
page_image_instance = PageImage.from_json(json)
# print the JSON string representation of the object
print(PageImage.to_json())

# convert the object into a dict
page_image_dict = page_image_instance.to_dict()
# create an instance of PageImage from a dict
page_image_from_dict = PageImage.from_dict(page_image_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


