# CreateEmailDomainRequest

The domain to add.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain name, such as `example.com` or `mail.example.com`. Email actions can send from any address at it. | 

## Example

```python
from docspring.models.create_email_domain_request import CreateEmailDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailDomainRequest from a JSON string
create_email_domain_request_instance = CreateEmailDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEmailDomainRequest.to_json())

# convert the object into a dict
create_email_domain_request_dict = create_email_domain_request_instance.to_dict()
# create an instance of CreateEmailDomainRequest from a dict
create_email_domain_request_from_dict = CreateEmailDomainRequest.from_dict(create_email_domain_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


