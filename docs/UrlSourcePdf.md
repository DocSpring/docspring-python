# UrlSourcePdf

A PDF to download from a URL and merge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Must be `url`. | [default to 'url']
**url** | **str** | For a `url` source, the URL to download the PDF from. Removed once the combined PDF has expired. | 

## Example

```python
from docspring.models.url_source_pdf import UrlSourcePdf

# TODO update the JSON string below
json = "{}"
# create an instance of UrlSourcePdf from a JSON string
url_source_pdf_instance = UrlSourcePdf.from_json(json)
# print the JSON string representation of the object
print(UrlSourcePdf.to_json())

# convert the object into a dict
url_source_pdf_dict = url_source_pdf_instance.to_dict()
# create an instance of UrlSourcePdf from a dict
url_source_pdf_from_dict = UrlSourcePdf.from_dict(url_source_pdf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


