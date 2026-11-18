# SupportHelp

A question put to DocSpring's AI help, and its answer from DocSpring's documentation. It opens no ticket and reaches no person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The help request's ID. | 
**state** | [**SupportHelpState**](SupportHelpState.md) | `pending` until there's an answer, then `completed`. `failed`: the question couldn't be answered just now. | 
**answered** | **bool** | Whether the documentation had an answer. Null while `state` is `pending`. | 
**answer** | **str** | The answer, as plain text. When `answered` is false, what the documentation doesn't cover. Null while `state` is `pending`. | 
**sources** | [**List[SupportHelpSource]**](SupportHelpSource.md) | The documentation pages the answer came from. | 
**next** | **str** | What to do when the answer doesn't solve the problem, in a sentence for an AI agent to act on. | 

## Example

```python
from docspring.models.support_help import SupportHelp

# TODO update the JSON string below
json = "{}"
# create an instance of SupportHelp from a JSON string
support_help_instance = SupportHelp.from_json(json)
# print the JSON string representation of the object
print(SupportHelp.to_json())

# convert the object into a dict
support_help_dict = support_help_instance.to_dict()
# create an instance of SupportHelp from a dict
support_help_from_dict = SupportHelp.from_dict(support_help_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


