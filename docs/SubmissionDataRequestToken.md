# SubmissionDataRequestToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**secret** | **str** |  | 
**expires_at** | **str** |  | 
**data_request_url** | **str** |  | 

## Example

```python
from docspring.models.submission_data_request_token import SubmissionDataRequestToken

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionDataRequestToken from a JSON string
submission_data_request_token_instance = SubmissionDataRequestToken.from_json(json)
# print the JSON string representation of the object
print(SubmissionDataRequestToken.to_json())

# convert the object into a dict
submission_data_request_token_dict = submission_data_request_token_instance.to_dict()
# create an instance of SubmissionDataRequestToken from a dict
submission_data_request_token_from_dict = SubmissionDataRequestToken.from_dict(submission_data_request_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


