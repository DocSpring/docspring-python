# SignatureRequestToken

A token that opens a signature request without signing in to DocSpring, in a form embedded in your app or from a link you send. Create a token each time you open the form or send a link, rather than storing one to reuse later: its link expires. A signing page that opened before then keeps working for 7 more days, so the person can finish the form later.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The token's ID. | 
**signature_request_id** | **str** | The ID of the signature request the token opens. | 
**type** | [**SignatureRequestTokenType**](SignatureRequestTokenType.md) | `api`: the link opens the signature request for 24 hours. `email`: 7 days. | 
**secret** | **str** | The token's secret. It's only returned when the token is created. | 
**signature_request_url** | **str** | A link that opens the signature request with this token. | 
**expires_at** | **datetime** | When the link stops opening the signature request. | 
**created_at** | **datetime** | When the token was created. | 

## Example

```python
from docspring.models.signature_request_token import SignatureRequestToken

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestToken from a JSON string
signature_request_token_instance = SignatureRequestToken.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestToken.to_json())

# convert the object into a dict
signature_request_token_dict = signature_request_token_instance.to_dict()
# create an instance of SignatureRequestToken from a dict
signature_request_token_from_dict = SignatureRequestToken.from_dict(signature_request_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


