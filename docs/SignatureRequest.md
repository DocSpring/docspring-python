# SignatureRequest

A request for someone to fill in their fields of a submission and sign it. Someone who only fills in fields for the people who sign later (such as an employer's section) has a signature request too. The submission's PDF is generated once every signature request is completed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The signature request's ID. | 
**submission_id** | **str** | The ID of the submission the signature request belongs to. | 
**name** | **str** | The name of the person the request is for. | 
**email** | **str** | Their email address. | 
**fields** | **List[str]** | The fields this person fills in. Null for a signature request created with API v1 without a field list: it asks for every field the submission's data doesn't have. | 
**metadata** | **Dict[str, object]** | Your own data about the signature request, such as an ID from your app. | 
**role** | **str** | Which of the template's signers the person is. Until templates have roles of their own, a template's signers are `Signer 1`, `Signer 2` and so on, up to `Signer 100`: `Signer 1` is the one whose details the template's `@@signature_requests/0` fields print. | 
**sort_order** | **int** | The signer's position, from 0: `Signer 1` is 0. The template's `@@signature_requests/&lt;sort_order&gt;` fields print this signature request's details. | 
**state** | [**SignatureRequestState**](SignatureRequestState.md) | `pending` until the person completes the signature request (`completed`) or declines it (`declined`). | 
**data** | **Dict[str, object]** | The values this person entered for their own fields (`fields`). Null when their submission's data is left out: in lists without `include_data=true`, in the events of a webhook that leaves out submission data, and once the submission has expired. | 
**viewed_at** | **datetime** | When the person first opened the signature request. | 
**completed_at** | **datetime** | When they completed it. | 
**declined_at** | **datetime** | When they declined it. | 
**auth_type** | [**SignatureRequestAuthType**](SignatureRequestAuthType.md) | How your app authenticated the person before it showed them the signature request. | 
**auth_second_factor_type** | [**SignatureRequestAuthSecondFactorType**](SignatureRequestAuthSecondFactorType.md) | The second factor your app authenticated them with, if any. | 
**auth_provider** | **str** | The service that authenticated them, such as `google`. Required when `auth_type` is `oauth`. | 
**auth_session_started_at** | **datetime** | When your app authenticated them. Set for you with `email_link`. | 
**auth_session_id_hash** | **str** | A hash of your app's session ID, for the audit trail. | 
**auth_user_id_hash** | **str** | Their user ID in your app, or a SHA-256 hash of a salt and the user ID. | 
**auth_username_hash** | **str** | Their username in your app, or a SHA-256 hash of a salt and the username. | 
**auth_phone_number_hash** | **str** | The phone number they authenticated with, or a SHA-256 hash of a salt and the phone number. | 
**ip_address** | **str** | The IP address they completed the signature request from. Null in the events of a webhook that leaves out submission data. | 
**user_agent** | **str** | The User-Agent header of the browser they completed the signature request with. Null in the events of a webhook that leaves out submission data. | 
**created_at** | **datetime** | When the signature request was created. | 
**updated_at** | **datetime** | When the signature request was last updated. | 

## Example

```python
from docspring.models.signature_request import SignatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequest from a JSON string
signature_request_instance = SignatureRequest.from_json(json)
# print the JSON string representation of the object
print(SignatureRequest.to_json())

# convert the object into a dict
signature_request_dict = signature_request_instance.to_dict()
# create an instance of SignatureRequest from a dict
signature_request_from_dict = SignatureRequest.from_dict(signature_request_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


