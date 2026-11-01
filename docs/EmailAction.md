# EmailAction

Emails each submission's files (its PDF, and a Word template's Word document and OpenDocument file) to people when the submission has been processed. An email action belongs to a template's draft, or to your account (an account email action, with no `template_id`), which sends for every template or for the templates and folders it lists. Each template can turn an account email action off or change its settings for that template only (`customization`). Email actions email anyone on a paid plan (Starter or higher); without one, they only email your team (test emails, and test submissions). They send from DocSpring's shared address or from one of your verified email domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The email action's ID. | 
**template_id** | **str** | The ID of the template it belongs to. Null for an account email action, which sends for many templates. | 
**template_ids** | **List[str]** | For an account email action: the IDs of the templates it sends for. With `folder_ids`, it sends for a template that either list includes. Both empty sends for every template. Always empty for a template's own email action. | 
**folder_ids** | **List[str]** | For an account email action: the IDs of folders whose templates it sends for, including the templates in the folders inside them. Always empty for a template's own email action. | 
**name** | **str** | A name for the email action, shown in the dashboard. Null shows its recipients instead. | 
**enabled** | **bool** | Whether it sends emails. DocSpring turns an email action off after 3 days of failed emails, or straight away when one of the addresses in `to`, `cc` or `bcc` (not one from a field or metadata) bounces or marks an email as spam. | 
**to** | **List[str]** | Who gets each email: email addresses, and tags for an address that each submission gives, from one of the template's text or email fields (`{{ data.client_email }}`, or `{{ data["client email"] }}` for a name with spaces) or from its metadata (`{{ metadata.agent_email }}`, or `{{ metadata.agent.email }}` for a value in an object). A tag whose value is blank or isn't a valid address is skipped for that submission, and so is a field an account email action names that the template doesn't have. `{{ signer.email }}` sends each of the submission's signers their own email, to them alone, and everyone else in `to`, `cc` and `bcc` one email together, without the signers. An email needs at least one entry in `to`, `cc` or `bcc`, and at most 10 across them. | 
**cc** | **List[str]** | Who is copied on each email, as in `to` (but not `{{ signer.email }}`). | 
**bcc** | **List[str]** | Who is blind-copied on each email, as in `to` (but not `{{ signer.email }}`). | 
**from_name** | **str** | The sender's name. Null uses your account's name. From DocSpring's shared address, the name is followed by "via DocSpring". | 
**from_address** | **str** | The sender's address, at one of your verified email domains. Null sends from DocSpring's shared address. | 
**reply_to** | **str** | Where replies go: a team member's email address, or an address at one of your verified email domains. Null sends without a reply address. | 
**subject** | **str** | The subject line, a Liquid template with the variables `account.name`, `template.name`, `template.id`, `submission.id`, the submission's values as `data.&lt;field name&gt;` (`data["field name"]` for a name with spaces) and its metadata as `metadata.&lt;key&gt;`, such as `Your {{ template.name }}`. Null uses the template's name followed by the file it sends, such as "Lease PDF", or by "files" when it sends several. | 
**message** | **str** | The email's text, a Liquid template with the same variables as `subject`. `if`, `unless` and `case` tags work. Line breaks are kept. Null uses a short message that says the files are attached or ready to download. | 
**file_name** | **str** | The attached files' name, a Liquid template with the same variables as `subject`, such as `{{ data.last_name }} lease`. Each file's extension (`.pdf`, `.docx` or `.odt`) is added. Null uses the submission's `pdf_filename` metadata when it has one, and otherwise the template's name. A download link's files have the names their other downloads have: the submission's `pdf_filename`, or its ID. | 
**file_formats** | [**EmailActionFileFormats**](EmailActionFileFormats.md) | Which of the submission's files the email sends: `all` sends every file the submission made (its PDF, and a Word template's Word document and OpenDocument file when it made them), and `docx`, `odt` or `pdf` sends only that file. A submission that made none of them sends nothing, and its email shows as skipped. Only Word templates make Word documents and OpenDocument files, so another template's email action takes `pdf` or `all`. | 
**delivery** | [**EmailActionDelivery**](EmailActionDelivery.md) | `attachment` attaches the files, or sends a download link when together they're larger than `max_attachment_mb`. `link` sends a download link, which works for 7 days. Accounts with a BAA start with `link`. | 
**max_attachment_mb** | **int** | With `delivery` `attachment`, files larger than this many megabytes in all (1 MB is 1,000,000 bytes) are sent as a download link instead. Emailing a file makes it about 38% larger, and many company mail servers refuse emails over 10 MB, so the default is 7. Raise it only when every recipient's mail server accepts larger emails, such as Microsoft 365 (up to 36 MB) or Gmail (50 MB). | 
**submission_type** | [**EmailActionSubmissionType**](EmailActionSubmissionType.md) | Which submissions send emails: `live`, `test` or `all`. Test submissions only email your team's members, and skip every other recipient. | 
**send_when** | [**EmailActionConditions**](EmailActionConditions.md) | Sends the email only when the submission's values meet these conditions, which work as a conditional logic rule's do. The values are the ones the PDF has: formulas worked out, and blank for a field that a rule hides. A field the template doesn't have (in an account email action's conditions) counts as blank. A submission that doesn't meet them sends nothing, and its email shows as skipped. Null sends for every submission. | 
**failure_notifications_enabled** | **bool** | Whether the account's owner gets an email when the email action's emails keep failing. | 
**consecutive_failures** | **int** | How many emails in a row have failed. | 
**failing_since** | **datetime** | When the current run of failures started. Null when the last email was sent. | 
**last_failure_at** | **datetime** | When an email last failed. | 
**last_failure_message** | **str** | Why the last failed email failed. | 
**disabled_at** | **datetime** | When the email action was turned off. Null while it is on. | 
**disabled_reason** | **str** | Why DocSpring turned the email action off, such as after 3 days of failed emails or an address that bounced. | 
**customization** | [**EmailActionCustomization**](EmailActionCustomization.md) | In a template's list of email actions, its changes to an account email action, or null when it changes nothing. The email action's settings are then the ones it sends for that template. Null everywhere else. | 
**created_at** | **datetime** | When the email action was created. | 
**updated_at** | **datetime** | When the email action was last changed. | 

## Example

```python
from docspring.models.email_action import EmailAction

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAction from a JSON string
email_action_instance = EmailAction.from_json(json)
# print the JSON string representation of the object
print(EmailAction.to_json())

# convert the object into a dict
email_action_dict = email_action_instance.to_dict()
# create an instance of EmailAction from a dict
email_action_from_dict = EmailAction.from_dict(email_action_dict)
```
[[Back to Model list]](../README.md#methods) [[Back to API list]](../README.md#methods) [[Back to README]](../README.md)


