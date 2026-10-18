# CombinePdfsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_custom_files** | **bool** | Delete the custom files in source_pdfs once the combined PDF has been processed (they&#39;re kept if it fails). Other combined submissions can&#39;t use them after that. A test API token can&#39;t delete custom files. | [optional] 
**expires_in** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 
**password** | **str** |  | [optional] 
**source_pdfs** | **List[object]** |  | 
**test** | **bool** | Deprecated, and has no effect. Combining always uses credits, even with a test API token or watermarked source PDFs. | [optional] 

## Example

```python
from docspring.models.combine_pdfs_data import CombinePdfsData

# TODO update the JSON string below
json = "{}"
# create an instance of CombinePdfsData from a JSON string
combine_pdfs_data_instance = CombinePdfsData.from_json(json)
# print the JSON string representation of the object
print(CombinePdfsData.to_json())

# convert the object into a dict
combine_pdfs_data_dict = combine_pdfs_data_instance.to_dict()
# create an instance of CombinePdfsData from a dict
combine_pdfs_data_from_dict = CombinePdfsData.from_dict(combine_pdfs_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


