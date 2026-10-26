# SubmissionInput

A submission to create in a batch, with its own template when it doesn't use the batch's.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | **bool** | Test PDFs have a watermark and are free. Live PDFs use credits. Submissions made with a test API token are always test submissions. | [optional] 
**editable** | **bool** | `true` keeps the PDF's text and check fields fillable, and `false` flattens every field. Left out, the template decides: its `editable_submissions` setting, or each field's own Editable option. A response shows the template's setting when the request left this out. Can't be `true` with `signature_requests`. | [optional] 
**data** | **Dict[str, object]** | The values of the template's fields, by field name. Required for a PDF template. | [optional] 
**metadata** | **Dict[str, object]** | Your own data about the submission, such as an ID from your app. It isn't printed on the PDF. | [optional] 
**password** | **str** | A password that the PDF needs to be opened with. It's never returned; `has_password` says if it's set. | [optional] 
**output_formats** | [**List[OutputFormat]**](OutputFormat.md) | What the submission makes: `pdf`, and `png` (an image of each page of the PDF, up to 100 pages) when you ask for it. Default `["pdf"]`. POST /submissions/{submission_id}/generate_files adds `png` to a processed submission. | [optional] 
**expires_in** | **int** | Seconds after the PDF is generated until the submission expires, up to 10 years (315360000). Default the template's expiration setting. A submission that isn't processed, such as one with invalid data, is kept for at least 48 hours. | [optional] 
**field_overrides** | [**Dict[str, FieldOverride]**](FieldOverride.md) | Changes to field settings for this submission only, by field name, such as `{"name": {"required": false, "font_size": 9}}`. A setting that identifies the field (`id`, `name`, `type`), that only the template sets (such as `description`), or that doesn't apply to the field's type and display type (such as `check_character` on a field displayed as text) is a 422. With `signature_requests`, `editable: true` is a 422, and a `default` for a signature or initials field makes the submission `invalid_data`. | [optional] 
**html** | **str** | For an HTML template, HTML to use instead of the template's. | [optional] 
**css** | **str** | For an HTML template, CSS to use instead of the template's. | [optional] 
**template_id** | **str** | The submission's template. Default the batch's `template_id`. | [optional] 
**template_version** | **str** | The version of the submission's template. Default the batch's `template_version`. | [optional] 

## Example

```python
from docspring.models.submission_input import SubmissionInput

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionInput from a JSON string
submission_input_instance = SubmissionInput.from_json(json)
# print the JSON string representation of the object
print(SubmissionInput.to_json())

# convert the object into a dict
submission_input_dict = submission_input_instance.to_dict()
# create an instance of SubmissionInput from a dict
submission_input_from_dict = SubmissionInput.from_dict(submission_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


