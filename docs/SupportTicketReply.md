# SupportTicketReply

A reply that was added to a support ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket** | [**SupportTicket**](SupportTicket.md) |  | 
**message** | [**SupportMessage**](SupportMessage.md) |  | 

## Example

```python
from docspring.models.support_ticket_reply import SupportTicketReply

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketReply from a JSON string
support_ticket_reply_instance = SupportTicketReply.from_json(json)
# print the JSON string representation of the object
print(SupportTicketReply.to_json())

# convert the object into a dict
support_ticket_reply_dict = support_ticket_reply_instance.to_dict()
# create an instance of SupportTicketReply from a dict
support_ticket_reply_from_dict = SupportTicketReply.from_dict(support_ticket_reply_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


