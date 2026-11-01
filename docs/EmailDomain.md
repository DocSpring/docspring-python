# EmailDomain

A domain your email actions can send from once it's verified. Add its DNS records where you manage the domain's DNS: DocSpring checks for them every few minutes, and the domain is verified once its DKIM and DMARC records are found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The email domain's ID. | 
**domain** | **str** | The domain name, such as `example.com` or `mail.example.com`. Email actions can send from any address at it. | 
**state** | [**EmailDomainState**](EmailDomainState.md) | `pending` until its DNS records are found, then `verified`. `failed`: its records weren't found within 3 days, or were removed. Verify it again after fixing them. | 
**dkim_state** | [**EmailDomainRecordState**](EmailDomainRecordState.md) | Whether the DKIM records were found. | 
**mail_from_state** | [**EmailDomainRecordState**](EmailDomainRecordState.md) | Whether the MAIL FROM records were found. They're optional: they let SPF pass for your domain too. | 
**dns_records** | [**List[EmailDomainDnsRecord]**](EmailDomainDnsRecord.md) | The DNS records to add to the domain. Empty while DocSpring is still setting the domain up: verify it again in a few minutes to get them. | 
**dmarc_policy** | **str** | The policy (`p=`) of the domain's DMARC record, once it has been found. | 
**last_error** | **str** | Why the domain isn't verified yet, or what to fix. | 
**verified_at** | **datetime** | When the domain was verified. | 
**checked_at** | **datetime** | When DocSpring last checked the domain's DNS records. | 
**created_at** | **datetime** | When the domain was added. | 

## Example

```python
from docspring.models.email_domain import EmailDomain

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomain from a JSON string
email_domain_instance = EmailDomain.from_json(json)
# print the JSON string representation of the object
print(EmailDomain.to_json())

# convert the object into a dict
email_domain_dict = email_domain_instance.to_dict()
# create an instance of EmailDomain from a dict
email_domain_from_dict = EmailDomain.from_dict(email_domain_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


