# SupportTicketNotifications

How the team's reply to a support ticket arrives.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The masked address of the user the reply is emailed to: the user the API token or connected app belongs to. Null when that user was removed. | 
**watch** | [**SupportTicketWatch**](SupportTicketWatch.md) |  | 

## Example

```python
from docspring.models.support_ticket_notifications import SupportTicketNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketNotifications from a JSON string
support_ticket_notifications_instance = SupportTicketNotifications.from_json(json)
# print the JSON string representation of the object
print(SupportTicketNotifications.to_json())

# convert the object into a dict
support_ticket_notifications_dict = support_ticket_notifications_instance.to_dict()
# create an instance of SupportTicketNotifications from a dict
support_ticket_notifications_from_dict = SupportTicketNotifications.from_dict(support_ticket_notifications_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


