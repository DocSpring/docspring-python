# ReplyToSupportTicketRequest

A message to add to the ticket. Never include secrets, credentials or your users' data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The message: an answer to the team's question, more detail, or whether their fix worked. Plain text. | 
**outcome** | [**SupportTicketReplyOutcome**](SupportTicketReplyOutcome.md) | `resolved`: the problem is fixed, so close the ticket. `still_broken`: it isn't, so reopen the ticket. Without it, the reply answers a ticket that was waiting for one and otherwise leaves the status as it is. | [optional] 

## Example

```python
from docspring.models.reply_to_support_ticket_request import ReplyToSupportTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyToSupportTicketRequest from a JSON string
reply_to_support_ticket_request_instance = ReplyToSupportTicketRequest.from_json(json)
# print the JSON string representation of the object
print(ReplyToSupportTicketRequest.to_json())

# convert the object into a dict
reply_to_support_ticket_request_dict = reply_to_support_ticket_request_instance.to_dict()
# create an instance of ReplyToSupportTicketRequest from a dict
reply_to_support_ticket_request_from_dict = ReplyToSupportTicketRequest.from_dict(reply_to_support_ticket_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


