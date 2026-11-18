# SendSupportFeedbackRequest

Something about DocSpring that got in the way while the work still got done. Never include secrets, credentials or your users' data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | One line, written like an issue title. | 
**kind** | [**SupportReportKind**](SupportReportKind.md) | What kind of problem this is. | 
**category** | [**SupportReportCategory**](SupportReportCategory.md) | The part of DocSpring this is about. | [optional] 
**description** | **str** | What was tried, what was expected and what happened. | 
**impact** | [**SupportReportImpact**](SupportReportImpact.md) | `blocked`: the task could not be done. `worked_around`: it was done another way. `friction`: it was only slower. | [optional] 
**task** | **str** | What the user asked for, in a short phrase. | [optional] 
**request_ids** | **List[str]** | The request IDs of the requests that went wrong: `error.request_id` in an error response, or any response's `X-Request-Id` header. | [optional] 
**tool** | **str** | The API operation, MCP tool or CLI command involved. | [optional] 
**error** | **str** | The exact error text. | [optional] 
**suggestion** | **str** | What would have helped. | [optional] 
**source** | [**SupportReportSource**](SupportReportSource.md) | `user`: the user asked for this to be sent. `agent` (the default): an AI agent noticed the problem itself. | [optional] 
**session** | **str** | A label the sender chooses for its work, such as a session ID, a branch or a task name. When an account runs several agents at once, each can list only the tickets opened with its own label. | [optional] 
**agent** | [**SupportReportAgent**](SupportReportAgent.md) | The AI agent sending this, as it describes itself. Stored as unverified. | [optional] 

## Example

```python
from docspring.models.send_support_feedback_request import SendSupportFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendSupportFeedbackRequest from a JSON string
send_support_feedback_request_instance = SendSupportFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(SendSupportFeedbackRequest.to_json())

# convert the object into a dict
send_support_feedback_request_dict = send_support_feedback_request_instance.to_dict()
# create an instance of SendSupportFeedbackRequest from a dict
send_support_feedback_request_from_dict = SendSupportFeedbackRequest.from_dict(send_support_feedback_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


