# SignatureRequestInput

A request for someone to fill in their fields of a submission and sign it. Someone who only fills in fields for the people who sign later (such as an employer's section) has a signature request too. The submission's PDF is generated once every signature request is completed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the person the request is for. | [optional] 
**email** | **str** | Their email address. | [optional] 
**fields** | **List[str]** | The fields this person fills in. Each field can only be in one signature request, and a field that `data` fills in needs `prefilled_values_editable`. | 
**metadata** | **Dict[str, object]** | Your own data about the signature request, such as an ID from your app. | [optional] 
**role** | **str** | Which of the template's signers the person is: `Signer 1`, `Signer 2` and so on, up to `Signer 100`, until templates have roles of their own. Either every signature request has a `role` or none does, and each role can only have one. | [optional] 
**auth_type** | [**SignatureRequestAuthType**](SignatureRequestAuthType.md) | How your app authenticated the person before it showed them the signature request. | 
**auth_second_factor_type** | [**SignatureRequestAuthSecondFactorType**](SignatureRequestAuthSecondFactorType.md) | The second factor your app authenticated them with, if any. | [optional] 
**auth_provider** | **str** | The service that authenticated them, such as `google`. Required when `auth_type` is `oauth`. | [optional] 
**auth_session_started_at** | **datetime** | When your app authenticated them. Set for you with `email_link`. | [optional] 
**auth_session_id_hash** | **str** | A hash of your app's session ID, for the audit trail. | [optional] 
**auth_user_id_hash** | **str** | Their user ID in your app, or a SHA-256 hash of a salt and the user ID. | [optional] 
**auth_username_hash** | **str** | Their username in your app, or a SHA-256 hash of a salt and the username. | [optional] 
**auth_phone_number_hash** | **str** | The phone number they authenticated with, or a SHA-256 hash of a salt and the phone number. | [optional] 
**ignore_unknown_fields** | **bool** | Leave out names in `fields` that the template doesn't have, for one field list that you send with several templates. Without it, an unknown name makes the submission `invalid_data`. | [optional] 
**prefilled_values_editable** | **bool** | Let the person change the values that `data` already has for fields in `fields`. Without it, those fields are a 422. | [optional] 

## Example

```python
from docspring.models.signature_request_input import SignatureRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestInput from a JSON string
signature_request_input_instance = SignatureRequestInput.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestInput.to_json())

# convert the object into a dict
signature_request_input_dict = signature_request_input_instance.to_dict()
# create an instance of SignatureRequestInput from a dict
signature_request_input_from_dict = SignatureRequestInput.from_dict(signature_request_input_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


