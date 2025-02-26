# MultipleErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**errors** | **List[str]** |  | 

## Example

```python
from docspring.models.multiple_errors_response import MultipleErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleErrorsResponse from a JSON string
multiple_errors_response_instance = MultipleErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(MultipleErrorsResponse.to_json())

# convert the object into a dict
multiple_errors_response_dict = multiple_errors_response_instance.to_dict()
# create an instance of MultipleErrorsResponse from a dict
multiple_errors_response_from_dict = MultipleErrorsResponse.from_dict(multiple_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


