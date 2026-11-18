# AskSupportHelpRequest

A question about DocSpring. Never include secrets, credentials or your users' data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | What you want to know, in a sentence or two. For a follow-up question, include what was asked and answered before that matters to it: each request is answered by itself. | 
**tool** | **str** | The API operation, MCP tool or CLI command involved, if any. | [optional] 
**error** | **str** | The exact error text, if any. | [optional] 
**conversation** | [**List[SupportHelpTurn]**](SupportHelpTurn.md) | For a chat: the questions and answers so far, oldest first, when `question` follows on from them. At most 40 turns: start a new conversation after that. | [optional] 

## Example

```python
from docspring.models.ask_support_help_request import AskSupportHelpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskSupportHelpRequest from a JSON string
ask_support_help_request_instance = AskSupportHelpRequest.from_json(json)
# print the JSON string representation of the object
print(AskSupportHelpRequest.to_json())

# convert the object into a dict
ask_support_help_request_dict = ask_support_help_request_instance.to_dict()
# create an instance of AskSupportHelpRequest from a dict
ask_support_help_request_from_dict = AskSupportHelpRequest.from_dict(ask_support_help_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


