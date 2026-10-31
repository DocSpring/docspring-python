# SubmissionList

A page of submissions, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SubmissionSummary]**](SubmissionSummary.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.submission_list import SubmissionList

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionList from a JSON string
submission_list_instance = SubmissionList.from_json(json)
# print the JSON string representation of the object
print(SubmissionList.to_json())

# convert the object into a dict
submission_list_dict = submission_list_instance.to_dict()
# create an instance of SubmissionList from a dict
submission_list_from_dict = SubmissionList.from_dict(submission_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


