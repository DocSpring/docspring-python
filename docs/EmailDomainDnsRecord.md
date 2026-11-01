# EmailDomainDnsRecord

A DNS record to add to an email domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**EmailDomainDnsRecordPurpose**](EmailDomainDnsRecordPurpose.md) | What the record is for. `dkim` signs the emails (required), `mail_from` lets SPF pass for your domain (recommended), and `dmarc` tells inboxes what to do with emails that fail these checks (required). | 
**type** | [**DnsRecordType**](DnsRecordType.md) | The record's type. | 
**name** | **str** | The record's name. Some DNS hosts add the domain to the end of a name by themselves. | 
**value** | **str** | The record's value. | 

## Example

```python
from docspring.models.email_domain_dns_record import EmailDomainDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainDnsRecord from a JSON string
email_domain_dns_record_instance = EmailDomainDnsRecord.from_json(json)
# print the JSON string representation of the object
print(EmailDomainDnsRecord.to_json())

# convert the object into a dict
email_domain_dns_record_dict = email_domain_dns_record_instance.to_dict()
# create an instance of EmailDomainDnsRecord from a dict
email_domain_dns_record_from_dict = EmailDomainDnsRecord.from_dict(email_domain_dns_record_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


