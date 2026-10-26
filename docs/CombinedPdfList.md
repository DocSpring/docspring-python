# CombinedPdfList

A page of combined PDFs, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CombinedPdf]**](CombinedPdf.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.combined_pdf_list import CombinedPdfList

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedPdfList from a JSON string
combined_pdf_list_instance = CombinedPdfList.from_json(json)
# print the JSON string representation of the object
print(CombinedPdfList.to_json())

# convert the object into a dict
combined_pdf_list_dict = combined_pdf_list_instance.to_dict()
# create an instance of CombinedPdfList from a dict
combined_pdf_list_from_dict = CombinedPdfList.from_dict(combined_pdf_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


