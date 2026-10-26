# CreateCombinedPdfRequest

The PDFs to merge, and the combined PDF's settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_pdfs** | [**List[CombinedPdfSourceInput]**](CombinedPdfSourceInput.md) | The PDFs to merge, in order. | 
**metadata** | **Dict[str, object]** | Your own data about the combined PDF, such as an ID from your app. | [optional] 
**password** | **str** | A password that the PDF needs to be opened with. It's never returned; `has_password` says if it's set. | [optional] 
**delete_custom_files** | **bool** | Delete the custom files in `source_pdfs` once the combined PDF has been generated (they're kept if it fails). Other combined PDFs can't use them after that. A test API token can't delete custom files. | [optional] 
**expires_in** | **int** | Seconds after the PDF is generated until the combined PDF expires, up to 10 years (315360000). One that fails is kept for at least 48 hours. Without it, the combined PDF is kept until you delete it. | [optional] 

## Example

```python
from docspring.models.create_combined_pdf_request import CreateCombinedPdfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCombinedPdfRequest from a JSON string
create_combined_pdf_request_instance = CreateCombinedPdfRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCombinedPdfRequest.to_json())

# convert the object into a dict
create_combined_pdf_request_dict = create_combined_pdf_request_instance.to_dict()
# create an instance of CreateCombinedPdfRequest from a dict
create_combined_pdf_request_from_dict = CreateCombinedPdfRequest.from_dict(create_combined_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


