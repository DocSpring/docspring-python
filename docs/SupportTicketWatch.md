# SupportTicketWatch

How a script can wait for a support ticket to change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The ticket's `watch_url`. | 
**min_interval_seconds** | **int** | Poll no more often than this. | 
**how** | **str** | What to do with the URL, in a sentence for an AI agent to act on. | 

## Example

```python
from docspring.models.support_ticket_watch import SupportTicketWatch

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketWatch from a JSON string
support_ticket_watch_instance = SupportTicketWatch.from_json(json)
# print the JSON string representation of the object
print(SupportTicketWatch.to_json())

# convert the object into a dict
support_ticket_watch_dict = support_ticket_watch_instance.to_dict()
# create an instance of SupportTicketWatch from a dict
support_ticket_watch_from_dict = SupportTicketWatch.from_dict(support_ticket_watch_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


