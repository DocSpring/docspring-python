# TemplatePageProcessingStatus

How processing is going on one page of a PDF template's PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**TemplatePageImageStatus**](TemplatePageImageStatus.md) | The page's image, which the template editor shows. `pending` until it's rendered. | 
**fields** | [**TemplatePageFieldsStatus**](TemplatePageFieldsStatus.md) | Setting up the page's fields: `pending` while they're imported or detected, `naming` while AI names them, then `processed` or `failed`. `disabled` when DocSpring doesn't set up the page's fields. | 
**ai_naming** | [**TemplatePageAiNamingStatus**](TemplatePageAiNamingStatus.md) | `failed` or `skipped` when AI didn't name the page's fields as asked (`ai_error` says why), and the fields kept plain names. Null otherwise. | 
**ai_error** | [**TemplatePageAiError**](TemplatePageAiError.md) | Why AI naming failed or was skipped: `unavailable` (the AI service was unavailable: set up the fields again later), `error`, `credits` (the account had no free AI pages or credits left) or `skipped` (someone skipped AI setup in the template editor). Null when `ai_naming` is. | 
**detected_boxes** | **List[List[float]]** | While AI names the page's fields, the boxes field detection found: `[x, y, width, height]` in PDF points from the page's top-left corner. Null otherwise. | 

## Example

```python
from docspring.models.template_page_processing_status import TemplatePageProcessingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePageProcessingStatus from a JSON string
template_page_processing_status_instance = TemplatePageProcessingStatus.from_json(json)
# print the JSON string representation of the object
print(TemplatePageProcessingStatus.to_json())

# convert the object into a dict
template_page_processing_status_dict = template_page_processing_status_instance.to_dict()
# create an instance of TemplatePageProcessingStatus from a dict
template_page_processing_status_from_dict = TemplatePageProcessingStatus.from_dict(template_page_processing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


