# CreateSignatureRequestTokenRequest

The kind of link to make. Send no body for an `api` token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SignatureRequestTokenType**](SignatureRequestTokenType.md) | `api` (the default): the link opens the signature request for 24 hours, for a form your app opens or a link it gives the person right away. `email`: 7 days, for a link you send by email. | [optional] 

## Example

```python
from docspring.models.create_signature_request_token_request import CreateSignatureRequestTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSignatureRequestTokenRequest from a JSON string
create_signature_request_token_request_instance = CreateSignatureRequestTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSignatureRequestTokenRequest.to_json())

# convert the object into a dict
create_signature_request_token_request_dict = create_signature_request_token_request_instance.to_dict()
# create an instance of CreateSignatureRequestTokenRequest from a dict
create_signature_request_token_request_from_dict = CreateSignatureRequestTokenRequest.from_dict(create_signature_request_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


