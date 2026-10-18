# DocSpring Python SDK

The official Python client for the [DocSpring API](https://docspring.com/docs/api/). DocSpring fills PDF
templates with your data, generates PDFs from HTML templates, combines PDFs and collects e-signatures.

[Documentation](https://docspring.com/docs/) · [API reference](https://docspring.com/docs/api/) ·
[PyPI](https://pypi.org/project/docspring/) · [Changelog](https://github.com/DocSpring/docspring-python/blob/main/CHANGELOG.md)

Version 3.2.0. Requires Python >=3.9.

## Install and configure

Install the package:

```bash
pip install --upgrade docspring
```

Configure authentication via environment variables:

```bash
export DOCSPRING_TOKEN_ID="API_TOKEN_ID"
export DOCSPRING_TOKEN_SECRET="API_TOKEN_SECRET"
```

You can also configure the region or host. The host takes priority over the region:

```bash
export DOCSPRING_REGION="US" # US or EU (defaults to US)
export DOCSPRING_HOST="docspring.yourcompany.com" # For on-premise deployments
```

Import and initialize the DocSpring client:

```python
from docspring import Client
client = Client()
```

Or provide credentials directly:

```python
from docspring import Client
client = Client(api_token_id='API_TOKEN_ID', api_token_secret='API_TOKEN_SECRET')
```

## Generate a PDF

Fill a template with data (use your template's ID in place of `tpl_1234567890abcdef01`):

```python
template_id = "tpl_1234567890abcdef01"
submission = {
    "data": {
        "first_name": "John",
        "last_name": "Smith",
        "phone_number": "+11234567890",
    },
    "metadata": {"foo": 123, "bar": "baz"},
}
wait = None

response = client.generate_pdf(template_id, submission, wait=wait)
print(response)
```

By default the call waits for the PDF, for up to 95 seconds, and the submission in the response has its
`download_url`. Set `wait` to false to get a pending submission straight away.
[Sync vs. async processing](https://docspring.com/docs/api-guide/synchronous-requests/) covers the time limit, status
checks and webhooks.

## Methods

[docs/Client.md](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md) has each method's parameters and return type, and
[docs/](https://github.com/DocSpring/docspring-python/tree/main/docs) has the models. The [API reference](https://docspring.com/docs/api/) has
Python code for every method.

| Method | Description |
| ------ | ----------- |
| [`add_fields_to_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#add_fields_to_template) | Add new fields to a Template |
| [`batch_generate_pdfs`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#batch_generate_pdfs) | Generate multiple PDFs |
| [`combine_pdfs`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#combine_pdfs) | Merge submission PDFs, template PDFs, or custom files |
| [`copy_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#copy_template) | Copy a template |
| [`create_custom_file_from_upload`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_custom_file_from_upload) | Create a new custom file from a cached S3 upload |
| [`create_data_request_event`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_data_request_event) | Create a new event for emailing a signee a request for signature |
| [`create_data_request_token`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_data_request_token) | Create a new data request token for form authentication |
| [`create_folder`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_folder) | Create a folder |
| [`create_html_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_html_template) | Create a new HTML template |
| [`create_pdf_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_pdf_template) | Create a new PDF template with a form POST file upload |
| [`create_pdf_template_from_upload`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_pdf_template_from_upload) | Create a new PDF template from a cached S3 file upload |
| [`create_webhook`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#create_webhook) | Create a webhook |
| [`delete_folder`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#delete_folder) | Delete a folder |
| [`delete_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#delete_template) | Delete a template |
| [`delete_webhook`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#delete_webhook) | Delete a webhook |
| [`expire_combined_submission`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#expire_combined_submission) | Expire a combined submission |
| [`expire_submission`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#expire_submission) | Expire a PDF submission |
| [`generate_pdf`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#generate_pdf) | Generate a PDF |
| [`generate_preview`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#generate_preview) | Generate a preview PDF for partially completed data requests |
| [`get_combined_submission`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_combined_submission) | Check the status of a combined submission (merged PDFs) |
| [`get_data_request`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_data_request) | Look up a submission data request |
| [`get_full_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_full_template) | Fetch the full attributes for a PDF template |
| [`get_presign_url`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_presign_url) | Get a presigned S3 URL for direct file upload |
| [`get_submission`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_submission) | Check the status of a PDF |
| [`get_submission_batch`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_submission_batch) | Check the status of a submission batch job |
| [`get_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_template) | Check the status of an uploaded template |
| [`get_template_model_code`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_template_model_code) | Generate typed model code for a template |
| [`get_template_schema`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_template_schema) | Fetch the JSON schema for a template |
| [`get_webhook`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#get_webhook) | Get a webhook |
| [`list_combined_submissions`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_combined_submissions) | Get a list of all combined submissions |
| [`list_folders`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_folders) | Get a list of all folders |
| [`list_submissions`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_submissions) | List all submissions |
| [`list_template_submissions`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_template_submissions) | List all submissions for a given template |
| [`list_templates`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_templates) | Get a list of all templates |
| [`list_webhooks`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#list_webhooks) | Get a list of all webhooks |
| [`move_folder_to_folder`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#move_folder_to_folder) | Move a folder |
| [`move_template_to_folder`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#move_template_to_folder) | Move Template to folder |
| [`publish_template_version`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#publish_template_version) | Publish a template version |
| [`rename_folder`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#rename_folder) | Rename a folder |
| [`restore_template_version`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#restore_template_version) | Restore a template version |
| [`test_authentication`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#test_authentication) | Test authentication |
| [`update_data_request`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#update_data_request) | Update a submission data request |
| [`update_template`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#update_template) | Update a Template |
| [`update_template_document`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#update_template_document) | Update a template's document with a form POST file upload |
| [`update_template_document_from_upload`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#update_template_document_from_upload) | Update a template's document with a cached S3 file upload |
| [`update_webhook`](https://github.com/DocSpring/docspring-python/blob/main/docs/Client.md#update_webhook) | Update a webhook |

## Errors

Methods raise `docspring.ApiException` for an error response (or a subclass from `docspring.exceptions`, such as `NotFoundException`), with the HTTP status in `status` and the body in `body`.

## API changes

DocSpring adds fields and enum values to API v1 without releasing a new API version. Changes that would break
existing code, such as removing or renaming a field, go in a new API version
([API changes](https://docspring.com/docs/api-guide/openapi-schema/#api-changes)). So this SDK keeps working with
responses that are newer than it is:

- The model keeps a response field added to the API after this release in its `additional_properties` dict.
- An enum value added to the API after this release comes back as a string, so handle values you don't recognize.

Upgrade the SDK to read new fields and enum values. The [changelog](https://github.com/DocSpring/docspring-python/blob/main/CHANGELOG.md) lists
what each release adds.

## About this SDK

This SDK is generated from DocSpring's [OpenAPI spec](https://docspring.com/api-docs/v1/openapi.json) with
[DocSpring's fork of OpenAPI Generator](https://github.com/DocSpring/openapi-generator/tree/docspring/all_patches) 7.16.0.
The fork changes the Python generator:

- Responses with an enum value added to the API after this release don't raise `ValueError`. Creating a model yourself still checks its values.

On top of the generated code, we add:

- A client constructor that reads your credentials, region and host from the environment.

Because the code is generated, we can't merge pull requests that change it. Please
[open an issue](https://github.com/DocSpring/docspring-python/issues) or email [support@docspring.com](mailto:support@docspring.com) instead, and
we'll fix it in the generator. [AGENTS.md](https://github.com/DocSpring/docspring-python/blob/main/AGENTS.md) is a short guide for AI coding agents.

## License

MIT. See [LICENSE](https://github.com/DocSpring/docspring-python/blob/main/LICENSE).
