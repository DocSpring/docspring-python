# PageImages

A PNG image of each page of the submission's PDF (the `png` output format), at 140 DPI: a US Letter page is 1190 x 1540 pixels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**GeneratedFileState**](GeneratedFileState.md) | `processed` once the images have been made, with the PDF or by POST /submissions/{submission_id}/generate_files. `pending` until then, and `error` if they couldn't be made (see `error_message`). | 
**error_message** | **str** | Why the images couldn't be made, when `state` is `error`. | 
**page_count** | **int** | How many pages have an image. Null until the images have been made. | 
**pages** | [**List[PageImage]**](PageImage.md) | An image of each page, in order: `pages[0]` is page 1. Lists of submissions leave it out (null): get the submission to see them. Empty until the images have been made. | 

## Example

```python
from docspring.models.page_images import PageImages

# TODO update the JSON string below
json = "{}"
# create an instance of PageImages from a JSON string
page_images_instance = PageImages.from_json(json)
# print the JSON string representation of the object
print(PageImages.to_json())

# convert the object into a dict
page_images_dict = page_images_instance.to_dict()
# create an instance of PageImages from a dict
page_images_from_dict = PageImages.from_dict(page_images_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


