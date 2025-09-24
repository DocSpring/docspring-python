# ErrorOrMultipleErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**error** | **str** | Single error message (when only one error occurred) | [optional] 
**errors** | **List[str]** | Array of error messages (when multiple validation errors occurred) | [optional] 

## Example

```python
from docspring.models.error_or_multiple_errors_response import ErrorOrMultipleErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorOrMultipleErrorsResponse from a JSON string
error_or_multiple_errors_response_instance = ErrorOrMultipleErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorOrMultipleErrorsResponse.to_json())

# convert the object into a dict
error_or_multiple_errors_response_dict = error_or_multiple_errors_response_instance.to_dict()
# create an instance of ErrorOrMultipleErrorsResponse from a dict
error_or_multiple_errors_response_from_dict = ErrorOrMultipleErrorsResponse.from_dict(error_or_multiple_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


