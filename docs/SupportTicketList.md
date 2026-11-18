# SupportTicketList

A page of support tickets, most recently updated first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SupportTicket]**](SupportTicket.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.support_ticket_list import SupportTicketList

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketList from a JSON string
support_ticket_list_instance = SupportTicketList.from_json(json)
# print the JSON string representation of the object
print(SupportTicketList.to_json())

# convert the object into a dict
support_ticket_list_dict = support_ticket_list_instance.to_dict()
# create an instance of SupportTicketList from a dict
support_ticket_list_from_dict = SupportTicketList.from_dict(support_ticket_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


