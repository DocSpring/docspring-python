# SuccessMultipleErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from docspring.models.success_multiple_errors_response import SuccessMultipleErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessMultipleErrorsResponse from a JSON string
success_multiple_errors_response_instance = SuccessMultipleErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessMultipleErrorsResponse.to_json())

# convert the object into a dict
success_multiple_errors_response_dict = success_multiple_errors_response_instance.to_dict()
# create an instance of SuccessMultipleErrorsResponse from a dict
success_multiple_errors_response_from_dict = SuccessMultipleErrorsResponse.from_dict(success_multiple_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


