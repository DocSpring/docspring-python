# CreateHtmlSubmissionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**css** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**editable** | **bool** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**field_overrides** | **object** |  | [optional] 
**html** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**password** | **str** |  | [optional] 
**test** | **bool** |  | [optional] 

## Example

```python
from docspring.models.create_html_submission_data import CreateHtmlSubmissionData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHtmlSubmissionData from a JSON string
create_html_submission_data_instance = CreateHtmlSubmissionData.from_json(json)
# print the JSON string representation of the object
print(CreateHtmlSubmissionData.to_json())

# convert the object into a dict
create_html_submission_data_dict = create_html_submission_data_instance.to_dict()
# create an instance of CreateHtmlSubmissionData from a dict
create_html_submission_data_from_dict = CreateHtmlSubmissionData.from_dict(create_html_submission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


