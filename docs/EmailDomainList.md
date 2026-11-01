# EmailDomainList

A page of the account's email domains, newest first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmailDomain]**](EmailDomain.md) | The items on this page. | 
**next_cursor** | **str** | Pass it as `cursor` to get the next page. Null on the last page. | 

## Example

```python
from docspring.models.email_domain_list import EmailDomainList

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainList from a JSON string
email_domain_list_instance = EmailDomainList.from_json(json)
# print the JSON string representation of the object
print(EmailDomainList.to_json())

# convert the object into a dict
email_domain_list_dict = email_domain_list_instance.to_dict()
# create an instance of EmailDomainList from a dict
email_domain_list_from_dict = EmailDomainList.from_dict(email_domain_list_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


