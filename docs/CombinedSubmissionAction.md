# CombinedSubmissionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**integration_id** | **str** |  | 
**state** | **str** |  | 
**action_type** | **str** |  | 
**action_category** | **str** |  | 
**result_data** | **object** |  | 

## Example

```python
from docspring.models.combined_submission_action import CombinedSubmissionAction

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedSubmissionAction from a JSON string
combined_submission_action_instance = CombinedSubmissionAction.from_json(json)
# print the JSON string representation of the object
print(CombinedSubmissionAction.to_json())

# convert the object into a dict
combined_submission_action_dict = combined_submission_action_instance.to_dict()
# create an instance of CombinedSubmissionAction from a dict
combined_submission_action_from_dict = CombinedSubmissionAction.from_dict(combined_submission_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


