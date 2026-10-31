# UpdateSignatureRequestRequest

The settings to change. Properties left out keep their values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Your own data about the signature request, such as an ID from your app. | [optional] 
**auth_type** | [**SignatureRequestAuthType**](SignatureRequestAuthType.md) | How your app authenticated the person before it showed them the signature request. | [optional] 
**auth_second_factor_type** | [**SignatureRequestAuthSecondFactorType**](SignatureRequestAuthSecondFactorType.md) | The second factor your app authenticated them with, if any. | [optional] 
**auth_provider** | **str** | The service that authenticated them, such as `google`. Required when `auth_type` is `oauth`. | [optional] 
**auth_session_started_at** | **datetime** | When your app authenticated them. Set for you with `email_link`. | [optional] 
**auth_session_id_hash** | **str** | A hash of your app's session ID, for the audit trail. | [optional] 
**auth_user_id_hash** | **str** | Their user ID in your app, or a SHA-256 hash of a salt and the user ID. | [optional] 
**auth_username_hash** | **str** | Their username in your app, or a SHA-256 hash of a salt and the username. | [optional] 
**auth_phone_number_hash** | **str** | The phone number they authenticated with, or a SHA-256 hash of a salt and the phone number. | [optional] 

## Example

```python
from docspring.models.update_signature_request_request import UpdateSignatureRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignatureRequestRequest from a JSON string
update_signature_request_request_instance = UpdateSignatureRequestRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSignatureRequestRequest.to_json())

# convert the object into a dict
update_signature_request_request_dict = update_signature_request_request_instance.to_dict()
# create an instance of UpdateSignatureRequestRequest from a dict
update_signature_request_request_from_dict = UpdateSignatureRequestRequest.from_dict(update_signature_request_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


