# docspring.Client

All URIs are relative to *https://sync.api.docspring.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_template_fields**](Client.md#add_template_fields) | **POST** /templates/{template_id}/fields | Add fields to a template
[**copy_template**](Client.md#copy_template) | **POST** /templates/{template_id}/copy | Copy a template
[**create_combined_pdf**](Client.md#create_combined_pdf) | **POST** /combined_pdfs | Combine PDFs
[**create_custom_file_from_upload**](Client.md#create_custom_file_from_upload) | **POST** /custom_files | Create a custom file from an upload
[**create_folder**](Client.md#create_folder) | **POST** /folders | Create a folder
[**create_signature_request_event**](Client.md#create_signature_request_event) | **POST** /signature_requests/{signature_request_id}/events | Record a signature request event
[**create_signature_request_token**](Client.md#create_signature_request_token) | **POST** /signature_requests/{signature_request_id}/tokens | Create a signature request token
[**create_submission**](Client.md#create_submission) | **POST** /templates/{template_id}/submissions | Generate a PDF
[**create_submission_batch**](Client.md#create_submission_batch) | **POST** /submissions/batches | Generate PDFs in a batch
[**create_template**](Client.md#create_template) | **POST** /templates | Create a template
[**create_template_preview**](Client.md#create_template_preview) | **POST** /templates/{template_id}/previews | Preview a template with data
[**create_webhook**](Client.md#create_webhook) | **POST** /webhooks | Create a webhook
[**delete_custom_file**](Client.md#delete_custom_file) | **DELETE** /custom_files/{custom_file_id} | Delete a custom file
[**delete_folder**](Client.md#delete_folder) | **DELETE** /folders/{folder_id} | Delete a folder
[**delete_template**](Client.md#delete_template) | **DELETE** /templates/{template_id} | Delete a template
[**delete_webhook**](Client.md#delete_webhook) | **DELETE** /webhooks/{webhook_id} | Delete a webhook
[**expire_combined_pdf**](Client.md#expire_combined_pdf) | **DELETE** /combined_pdfs/{combined_pdf_id} | Expire a combined PDF
[**expire_submission**](Client.md#expire_submission) | **DELETE** /submissions/{submission_id} | Expire a submission
[**generate_submission_files**](Client.md#generate_submission_files) | **POST** /submissions/{submission_id}/generate_files | Generate more files
[**generate_submission_preview**](Client.md#generate_submission_preview) | **POST** /submissions/{submission_id}/generate_preview | Generate a preview PDF
[**get_combined_pdf**](Client.md#get_combined_pdf) | **GET** /combined_pdfs/{combined_pdf_id} | Get a combined PDF
[**get_custom_file**](Client.md#get_custom_file) | **GET** /custom_files/{custom_file_id} | Get a custom file
[**get_folder**](Client.md#get_folder) | **GET** /folders/{folder_id} | Get a folder
[**get_presign_url**](Client.md#get_presign_url) | **GET** /uploads/presign | Get a presigned URL to upload a file
[**get_signature_request**](Client.md#get_signature_request) | **GET** /signature_requests/{signature_request_id} | Get a signature request
[**get_submission**](Client.md#get_submission) | **GET** /submissions/{submission_id} | Get a submission
[**get_submission_batch**](Client.md#get_submission_batch) | **GET** /submissions/batches/{submission_batch_id} | Get a batch
[**get_template**](Client.md#get_template) | **GET** /templates/{template_id} | Get a template
[**get_template_diff**](Client.md#get_template_diff) | **GET** /templates/{template_id}/diff | Compare a version of a template with the one before it
[**get_template_model_code**](Client.md#get_template_model_code) | **GET** /templates/{template_id}/model_code | Generate typed code for a template's submission data
[**get_template_page_images**](Client.md#get_template_page_images) | **GET** /templates/{template_id}/page_images | Get images of a template's pages
[**get_template_preview**](Client.md#get_template_preview) | **GET** /templates/{template_id}/previews/{preview_id} | Get a template preview
[**get_template_schema**](Client.md#get_template_schema) | **GET** /templates/{template_id}/schema | Get the JSON Schema of a template's submission data
[**get_webhook**](Client.md#get_webhook) | **GET** /webhooks/{webhook_id} | Get a webhook
[**list_combined_pdfs**](Client.md#list_combined_pdfs) | **GET** /combined_pdfs | List combined PDFs
[**list_custom_files**](Client.md#list_custom_files) | **GET** /custom_files | List custom files
[**list_folders**](Client.md#list_folders) | **GET** /folders | List folders
[**list_submissions**](Client.md#list_submissions) | **GET** /submissions | List submissions
[**list_template_fields**](Client.md#list_template_fields) | **GET** /templates/{template_id}/fields | List a template's fields
[**list_template_submissions**](Client.md#list_template_submissions) | **GET** /templates/{template_id}/submissions | List a template's submissions
[**list_templates**](Client.md#list_templates) | **GET** /templates | List templates
[**list_webhooks**](Client.md#list_webhooks) | **GET** /webhooks | List webhooks
[**move_folder**](Client.md#move_folder) | **POST** /folders/{folder_id}/move | Move a folder
[**move_template**](Client.md#move_template) | **POST** /templates/{template_id}/move | Move a template to a folder
[**publish_template_version**](Client.md#publish_template_version) | **POST** /templates/{template_id}/publish_version | Publish a template version
[**remove_template_fields**](Client.md#remove_template_fields) | **POST** /templates/{template_id}/fields/remove | Remove fields from a template
[**rename_folder**](Client.md#rename_folder) | **POST** /folders/{folder_id}/rename | Rename a folder
[**reorder_template_fields**](Client.md#reorder_template_fields) | **POST** /templates/{template_id}/fields/reorder | Reorder a template's fields
[**restore_template_version**](Client.md#restore_template_version) | **POST** /templates/{template_id}/restore_version | Restore a template version
[**test_authentication**](Client.md#test_authentication) | **GET** /authentication | Test authentication
[**update_signature_request**](Client.md#update_signature_request) | **PUT** /signature_requests/{signature_request_id} | Update a signature request
[**update_template**](Client.md#update_template) | **PUT** /templates/{template_id} | Update a template
[**update_template_document**](Client.md#update_template_document) | **PUT** /templates/{template_id}/document | Replace a template's document
[**update_template_fields**](Client.md#update_template_fields) | **PUT** /templates/{template_id}/fields | Update a template's fields
[**update_webhook**](Client.md#update_webhook) | **PUT** /webhooks/{webhook_id} | Update a webhook
[**upload_template**](Client.md#upload_template) | **POST** /templates/upload | Create a template from an uploaded PDF or Word document
[**upload_template_document**](Client.md#upload_template_document) | **PUT** /templates/{template_id}/document/upload | Replace a template's document with an uploaded file
[**validate_submission**](Client.md#validate_submission) | **POST** /templates/{template_id}/submissions/validate | Check a submission without creating it


# **add_template_fields**
> TemplateFields add_template_fields(template_id, body)

Add fields to a template

Adds fields to a template's draft and returns all of its fields. Publish a version for submissions of
published versions to have them.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.add_template_fields_request import AddTemplateFieldsRequest
from docspring.models.template_fields import TemplateFields
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"fields":[{"name":"email","page":1,"x":100,"y":300,"width":600,"height":80,"type":"email","required":true},{"name":"signature","page":1,"x":100,"y":400,"width":600,"height":150,"type":"signature","display_type":"image"}]} # AddTemplateFieldsRequest | The fields to add to the template's draft.

    try:
        # Add fields to a template
        api_response = api_instance.add_template_fields(template_id, body)
        print("The response of Client->add_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->add_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**AddTemplateFieldsRequest**](AddTemplateFieldsRequest.md)| The fields to add to the template's draft. | 

### Return type

[**TemplateFields**](TemplateFields.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | fields added |  -  |
**409** | the template's PDF hasn't been processed |  -  |
**422** | invalid fields |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **copy_template**
> Template copy_template(template_id, body=body)

Copy a template

Copies a template (its draft, or a published version) into a new template.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.copy_template_request import CopyTemplateRequest
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"parent_folder_id":"fld_1234567890abcdef01"} # CopyTemplateRequest | Settings for the copy. (optional)

    try:
        # Copy a template
        api_response = api_instance.copy_template(template_id, body=body)
        print("The response of Client->copy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->copy_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**CopyTemplateRequest**](CopyTemplateRequest.md)| Settings for the copy. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | template copied |  -  |
**422** | invalid copy |  -  |
**403** | the plan's template limit is reached |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_combined_pdf**
> CombinedPdf create_combined_pdf(body, wait=wait, idempotency_key=idempotency_key)

Combine PDFs

Merges PDFs into one: submissions, other combined PDFs, templates, custom files (POST /custom_files) and
PDFs from URLs, in the order of `source_pdfs`. The PDF is generated in the background: on sync.api hosts the
request waits for it (unless you pass `wait=false`), otherwise poll GET /combined_pdfs/{combined_pdf_id} until
`state` isn't `pending`.

A template source merges the template's processed PDF by default: the PDF submissions are filled in on,
decrypted and with its form fields removed. Pass `processed: false` to merge the PDF as it was uploaded.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_pdf import CombinedPdf
from docspring.models.create_combined_pdf_request import CreateCombinedPdfRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"source_pdfs":[{"type":"submission","id":"sub_1234567890abcdef01"},{"type":"template","id":"tpl_1234567890abcdef01"},{"type":"url","url":"https://example.com/terms.pdf"}],"metadata":{"user_id":42},"password":"secret","expires_in":3600} # CreateCombinedPdfRequest | The PDFs to merge, and the combined PDF's settings.
    wait = True # bool | Wait until the PDF has been generated before responding. Default true on sync.api hosts. (optional)
    idempotency_key = 'idempotency_key_example' # str | A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another combined PDF. Send a new key with each new combined PDF, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. (optional)

    try:
        # Combine PDFs
        api_response = api_instance.create_combined_pdf(body, wait=wait, idempotency_key=idempotency_key)
        print("The response of Client->create_combined_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_combined_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCombinedPdfRequest**](CreateCombinedPdfRequest.md)| The PDFs to merge, and the combined PDF's settings. | 
 **wait** | **bool**| Wait until the PDF has been generated before responding. Default true on sync.api hosts. | [optional] 
 **idempotency_key** | **str**| A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another combined PDF. Send a new key with each new combined PDF, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. | [optional] 

### Return type

[**CombinedPdf**](CombinedPdf.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | combined PDF created |  -  |
**422** | invalid source PDFs |  -  |
**403** | not allowed |  -  |
**402** | not enough credits |  -  |
**409** | a request with the same Idempotency-Key is still being processed |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's combined_pdf_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_custom_file_from_upload**
> CustomFile create_custom_file_from_upload(body)

Create a custom file from an upload

Creates a custom file from a PDF you uploaded, so you can merge it with other PDFs. Upload the file with the
presigned upload (GET /uploads/presign) first, then pass its `fields.key` as `cache_id`.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_custom_file_from_upload_request import CreateCustomFileFromUploadRequest
from docspring.models.custom_file import CustomFile
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"cache_id":"cfi_1234567890abcdef01.pdf"} # CreateCustomFileFromUploadRequest | The uploaded file to create the custom file from.

    try:
        # Create a custom file from an upload
        api_response = api_instance.create_custom_file_from_upload(body)
        print("The response of Client->create_custom_file_from_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_custom_file_from_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomFileFromUploadRequest**](CreateCustomFileFromUploadRequest.md)| The uploaded file to create the custom file from. | 

### Return type

[**CustomFile**](CustomFile.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | custom file created |  -  |
**422** | invalid custom file |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(body)

Create a folder

Creates a folder for organizing templates. Pass `parent_folder_id` to create it inside another folder.
Folder names are unique within their parent folder.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_folder_request import CreateFolderRequest
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"name":"Folder 3","parent_folder_id":"fld_1234567890abcdef01"} # CreateFolderRequest | The folder to create.

    try:
        # Create a folder
        api_response = api_instance.create_folder(body)
        print("The response of Client->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFolderRequest**](CreateFolderRequest.md)| The folder to create. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | folder created inside another folder |  -  |
**422** | invalid folder |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_signature_request_event**
> SignatureRequestEvent create_signature_request_event(signature_request_id, body)

Record a signature request event

Records something that happened outside DocSpring in the signature request's audit trail: you sent the request
to the person (`send_request`). The audit trail shows it as reported by your account. A finished (completed,
declined or expired) signature request's audit trail takes no more events, and a test API token can't record
one for a live signature request.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_signature_request_event_request import CreateSignatureRequestEventRequest
from docspring.models.signature_request_event import SignatureRequestEvent
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    signature_request_id = 'srq_1234567890abcdef01' # str | The signature request's ID.
    body = {"event_type":"send_request","message_type":"email","message_recipient":"john@example.com","occurred_at":"2018-10-20T08:59:00Z"} # CreateSignatureRequestEventRequest | The event to record.

    try:
        # Record a signature request event
        api_response = api_instance.create_signature_request_event(signature_request_id, body)
        print("The response of Client->create_signature_request_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_signature_request_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request_id** | **str**| The signature request's ID. | 
 **body** | [**CreateSignatureRequestEventRequest**](CreateSignatureRequestEventRequest.md)| The event to record. | 

### Return type

[**SignatureRequestEvent**](SignatureRequestEvent.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | event recorded |  -  |
**403** | test API token on a live signature request |  -  |
**409** | signature request finished |  -  |
**422** | invalid event |  -  |
**404** | signature request not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_signature_request_token**
> SignatureRequestToken create_signature_request_token(signature_request_id, body=body)

Create a signature request token

Creates a token that opens the signature request without signing in, in a form embedded in your app or from a
link you send. The response is the only time the token's secret is returned. The link works for 24 hours, or
7 days for an `email` token, and a signing page that opened in time keeps working for 7 more days. A test API
token can't create a token for a live signature request.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_signature_request_token_request import CreateSignatureRequestTokenRequest
from docspring.models.signature_request_token import SignatureRequestToken
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    signature_request_id = 'srq_1234567890abcdef01' # str | The signature request's ID.
    body = {"type":"email"} # CreateSignatureRequestTokenRequest | The kind of link to make. Send no body for an `api` token. (optional)

    try:
        # Create a signature request token
        api_response = api_instance.create_signature_request_token(signature_request_id, body=body)
        print("The response of Client->create_signature_request_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_signature_request_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request_id** | **str**| The signature request's ID. | 
 **body** | [**CreateSignatureRequestTokenRequest**](CreateSignatureRequestTokenRequest.md)| The kind of link to make. Send no body for an `api` token. | [optional] 

### Return type

[**SignatureRequestToken**](SignatureRequestToken.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | token created |  -  |
**403** | test API token on a live signature request |  -  |
**409** | signature request finished |  -  |
**422** | invalid token request |  -  |
**404** | signature request not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_submission**
> Submission create_submission(template_id, body, version=version, wait=wait, idempotency_key=idempotency_key)

Generate a PDF

Creates a submission: fills in a template with your data and generates a PDF. The PDF is generated in the
background: on sync.api hosts the request waits for it (unless you pass `wait=false`), otherwise poll GET
/submissions/{submission_id} until `state` isn't `pending`.

Data that doesn't match the template's fields returns a 422 with an `invalid_data` error. The submission
is still saved, with its errors, so you can find it in DocSpring: the error's `submission_id` is its ID.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_submission_request import CreateSubmissionRequest
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"data":{"first_name":"John","last_name":"Smith","phone_number":"+11234567890"},"metadata":{"user_id":42},"test":true} # CreateSubmissionRequest | The submission's data and settings.
    version = 'version_example' # str | The template version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). (optional)
    wait = True # bool | Wait until the files have been generated before responding. Default true on sync.api hosts. (optional)
    idempotency_key = 'idempotency_key_example' # str | A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another submission. Send a new key with each new submission, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. (optional)

    try:
        # Generate a PDF
        api_response = api_instance.create_submission(template_id, body, version=version, wait=wait, idempotency_key=idempotency_key)
        print("The response of Client->create_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**CreateSubmissionRequest**](CreateSubmissionRequest.md)| The submission's data and settings. | 
 **version** | **str**| The template version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). | [optional] 
 **wait** | **bool**| Wait until the files have been generated before responding. Default true on sync.api hosts. | [optional] 
 **idempotency_key** | **str**| A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another submission. Send a new key with each new submission, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | submission created |  -  |
**422** | invalid data |  -  |
**402** | not enough credits |  -  |
**403** | the account is suspended |  -  |
**404** | template not found |  -  |
**409** | a request with the same Idempotency-Key is still being processed |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's submission_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_submission_batch**
> SubmissionBatch create_submission_batch(body, wait=wait, idempotency_key=idempotency_key)

Generate PDFs in a batch

Creates up to 50 submissions in one request, from one template or several. The PDFs are only generated when
every submission is valid. On sync.api hosts the request waits until every PDF has been generated (unless you
pass `wait=false`), otherwise poll GET /submissions/batches/{submission_batch_id} until `processed_at` is set.

When any submission is invalid, nothing is generated and the request returns a 422. Submissions whose data
doesn't match their template's fields are still saved with their errors (an `invalid_data` error, with each
one's `submission_id` in its details), so you can find them in DocSpring. The other submissions aren't saved.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_submission_batch_request import CreateSubmissionBatchRequest
from docspring.models.submission_batch import SubmissionBatch
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"template_id":"tpl_1234567890abcdef01","metadata":{"job_id":54321},"submissions":[{"data":{"first_name":"John","last_name":"Smith"},"metadata":{"row":1}},{"data":{"first_name":"Jane","last_name":"Doe"},"test":true,"metadata":{"row":2}}]} # CreateSubmissionBatchRequest | The submissions to create, and the settings they share.
    wait = True # bool | Wait until every file in the batch has been generated before responding. Default true on sync.api hosts. (optional)
    idempotency_key = 'idempotency_key_example' # str | A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another batch. Send a new key with each new batch, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. (optional)

    try:
        # Generate PDFs in a batch
        api_response = api_instance.create_submission_batch(body, wait=wait, idempotency_key=idempotency_key)
        print("The response of Client->create_submission_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_submission_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubmissionBatchRequest**](CreateSubmissionBatchRequest.md)| The submissions to create, and the settings they share. | 
 **wait** | **bool**| Wait until every file in the batch has been generated before responding. Default true on sync.api hosts. | [optional] 
 **idempotency_key** | **str**| A key of your own, such as a UUID, that makes it safe to send this request again: for 24 hours, DocSpring answers a request with the same key from the same API token with the first request's response (and an `Idempotent-Replayed: true` header) instead of creating another batch. Send a new key with each new batch, and the same key each time you send the same request again, such as after a timeout, a network error or a 5xx. The same key with a different request is a 422 `idempotency_key_reused`. A 409 `idempotency_key_in_use` means the first request is still being processed: send the request again in a few seconds. | [optional] 

### Return type

[**SubmissionBatch**](SubmissionBatch.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | batch created |  -  |
**422** | invalid data |  -  |
**402** | not enough credits |  -  |
**403** | account suspended |  -  |
**409** | a request with the same Idempotency-Key is still being processed |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's submission_batch_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_template**
> Template create_template(body, wait=wait)

Create a template

Creates an HTML template, or a PDF or Word template from a file you uploaded with the presigned upload (GET
/uploads/presign): pass its `fields.key` as `cache_id`. You can send a link to the file (`document_url`) or
the file in base64 (`document_base64`) instead, or send the file with the request with POST
/templates/upload. A Word template is made from a Word document (.docx) or an OpenDocument text file (.odt),
which DocSpring converts to a Word document. It needs its `output_format`: what each submission makes, a Word
document (`docx`), an OpenDocument file (`odt`) or a PDF.

A PDF template is ready to generate PDFs once DocSpring has processed its PDF, a template created from a
`document_url` once its document has been downloaded, and one created from an .odt once it has been converted
(`ready` is true). On sync.api hosts the request waits for that unless you pass `wait=false`.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_template_request import CreateTemplateRequest
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"template_type":"html","name":"Receipt","html":"<h1>Receipt for {{ name }}</h1>","scss":"h1 { font-size: 24px; }","html_engine_options":{"format":"A4","landscape":true},"parent_folder_id":"fld_1234567890abcdef01"} # CreateTemplateRequest | The template to create.
    wait = True # bool | Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. (optional)

    try:
        # Create a template
        api_response = api_instance.create_template(body, wait=wait)
        print("The response of Client->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| The template to create. | 
 **wait** | **bool**| Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HTML template created |  -  |
**422** | invalid template |  -  |
**403** | the plan's template limit is reached |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's template_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_template_preview**
> TemplatePreview create_template_preview(template_id, body, version=version)

Preview a template with data

Makes PNG images of a template's pages filled in with the data you send (not a PDF), so you can check how an
HTML, PDF or Word template prints with your data before you publish a version or send live data. A Word
template's pages are its PDF's, whatever its `output_format`. It renders the template's draft, or the
published `version` you ask for. A preview makes no submission and uses no credits, and its pages are
watermarked like a test submission's PDF. It's `pending` while it renders: get it with GET
/templates/{template_id}/previews/{preview_id} until it's `processed`, with an image of each page, or `error`.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_template_preview_request import CreateTemplatePreviewRequest
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef02' # str | The template's ID.
    body = {"data":{"invoice_number":"INV-001"}} # CreateTemplatePreviewRequest | The data to render the template with.
    version = 'version_example' # str | A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. (optional)

    try:
        # Preview a template with data
        api_response = api_instance.create_template_preview(template_id, body, version=version)
        print("The response of Client->create_template_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_template_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**CreateTemplatePreviewRequest**](CreateTemplatePreviewRequest.md)| The data to render the template with. | 
 **version** | **str**| A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. | [optional] 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | preview created |  -  |
**409** | this server can't convert Word documents to PDF |  -  |
**422** | no data |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **create_webhook**
> Webhook create_webhook(body)

Create a webhook

Creates a webhook that sends a POST request to your endpoint whenever a subscribed event happens. Scope it to
API tokens, templates or folders to receive only their events.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_webhook_request import CreateWebhookRequest
from docspring.models.webhook import Webhook
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    body = {"name":"Test Webhook","url":"https://example.com/webhook","event_types":["submission.processed","signature_request.completed"],"template_ids":["tpl_1234567890abcdef01"],"headers":{"X-Zapier-Subscription":"123"}} # CreateWebhookRequest | The webhook to create.

    try:
        # Create a webhook
        api_response = api_instance.create_webhook(body)
        print("The response of Client->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebhookRequest**](CreateWebhookRequest.md)| The webhook to create. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | webhook created |  -  |
**422** | invalid webhook |  -  |
**403** | the plan's integration limit is reached |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **delete_custom_file**
> CustomFile delete_custom_file(custom_file_id)

Delete a custom file

Deletes a custom file and returns it. Use a live API token: test tokens can't delete custom files.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.custom_file import CustomFile
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    custom_file_id = 'custom_file_id_example' # str | The custom file's ID.

    try:
        # Delete a custom file
        api_response = api_instance.delete_custom_file(custom_file_id)
        print("The response of Client->delete_custom_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->delete_custom_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_id** | **str**| The custom file's ID. | 

### Return type

[**CustomFile**](CustomFile.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | custom file deleted |  -  |
**403** | test API token |  -  |
**404** | custom file not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **delete_folder**
> Folder delete_folder(folder_id)

Delete a folder

Deletes an empty folder and returns it. A folder that still has templates or folders in it can't be deleted.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    folder_id = 'folder_id_example' # str | The folder's ID.

    try:
        # Delete a folder
        api_response = api_instance.delete_folder(folder_id)
        print("The response of Client->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The folder's ID. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | folder deleted |  -  |
**409** | folder is not empty |  -  |
**404** | folder not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **delete_template**
> Template delete_template(template_id, version=version)

Delete a template

Deletes a template's draft and all of its published versions, or one published version (`version`). Returns
the template as it was before it was deleted.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef02' # str | The template's ID.
    version = 'version_example' # str | Delete only this published version (`1.2.0`) or the draft (`draft`, when no version has been published). Without it, the draft and every published version are deleted. (optional)

    try:
        # Delete a template
        api_response = api_instance.delete_template(template_id, version=version)
        print("The response of Client->delete_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| Delete only this published version (`1.2.0`) or the draft (`draft`, when no version has been published). Without it, the draft and every published version are deleted. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template deleted |  -  |
**409** | template is locked |  -  |
**404** | template not found |  -  |
**422** | invalid version |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **delete_webhook**
> Webhook delete_webhook(webhook_id)

Delete a webhook

Deletes a webhook so it stops receiving events, and returns it.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.webhook import Webhook
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    webhook_id = 'webhook_id_example' # str | The webhook's ID.

    try:
        # Delete a webhook
        api_response = api_instance.delete_webhook(webhook_id)
        print("The response of Client->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook's ID. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | webhook deleted |  -  |
**404** | webhook not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **expire_combined_pdf**
> CombinedPdf expire_combined_pdf(combined_pdf_id)

Expire a combined PDF

Deletes a combined PDF's PDF and returns the expired combined PDF.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_pdf import CombinedPdf
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    combined_pdf_id = 'com_1234567890abcdef05' # str | The combined PDF's ID.

    try:
        # Expire a combined PDF
        api_response = api_instance.expire_combined_pdf(combined_pdf_id)
        print("The response of Client->expire_combined_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->expire_combined_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_pdf_id** | **str**| The combined PDF's ID. | 

### Return type

[**CombinedPdf**](CombinedPdf.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | combined PDF expired |  -  |
**403** | test API token |  -  |
**404** | combined PDF not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **expire_submission**
> Submission expire_submission(submission_id)

Expire a submission

Deletes a submission's data and PDF now, and returns the expired submission.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | The submission's ID.

    try:
        # Expire a submission
        api_response = api_instance.expire_submission(submission_id)
        print("The response of Client->expire_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->expire_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| The submission's ID. | 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | submission expired |  -  |
**403** | test API token |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **generate_submission_files**
> Submission generate_submission_files(submission_id, body, wait=wait)

Generate more files

Adds formats to a processed submission's files, in the background, without using credits again: `pdf`, the
PDF of a Word template's submission that made only its Word document (converted from that document), `docx`,
the Word document of a Word template's submission that made only its PDF (made again from its data and the
template version it used), `odt`, a Word template's submission's OpenDocument file (converted from its Word
document, or from one made again when it didn't keep one), and `png`, a PNG image of each page of the PDF (up
to 100 pages), which makes the PDF first when the submission doesn't have one. To make them with the submission, add them to
`output_formats` when you create it.

Each new file is listed in `files` while it's made: on sync.api hosts the request waits for them (unless you
pass `wait=false`), otherwise poll GET /submissions/{submission_id} until none of their `state` is `pending`.
A file that couldn't be made has the state `error` and an `error_message`, and the submission stays
processed. Asking for a format the submission already has (or is making) changes nothing.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.generate_submission_files_request import GenerateSubmissionFilesRequest
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | The submission's ID.
    body = {"formats":["png"]} # GenerateSubmissionFilesRequest | The formats to make.
    wait = True # bool | Wait until the files have been generated before responding. Default true on sync.api hosts. (optional)

    try:
        # Generate more files
        api_response = api_instance.generate_submission_files(submission_id, body, wait=wait)
        print("The response of Client->generate_submission_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->generate_submission_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| The submission's ID. | 
 **body** | [**GenerateSubmissionFilesRequest**](GenerateSubmissionFilesRequest.md)| The formats to make. | 
 **wait** | **bool**| Wait until the files have been generated before responding. Default true on sync.api hosts. | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | images of the pages requested |  -  |
**409** | files not possible |  -  |
**422** | invalid request |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's submission_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **generate_submission_preview**
> Submission generate_submission_preview(submission_id)

Generate a preview PDF

Generates a preview of a submission's PDF in the background, such as for a submission still waiting for its
signature requests. It's in `files.preview` once `preview_generated_at` changes.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    submission_id = 'sub_1234567890abcdef03' # str | The submission's ID.

    try:
        # Generate a preview PDF
        api_response = api_instance.generate_submission_preview(submission_id)
        print("The response of Client->generate_submission_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->generate_submission_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| The submission's ID. | 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | preview requested |  -  |
**409** | preview not possible |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_combined_pdf**
> CombinedPdf get_combined_pdf(combined_pdf_id)

Get a combined PDF

Returns a combined PDF, with a temporary link to download it once it has been generated.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_pdf import CombinedPdf
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    combined_pdf_id = 'com_1234567890abcdef05' # str | The combined PDF's ID.

    try:
        # Get a combined PDF
        api_response = api_instance.get_combined_pdf(combined_pdf_id)
        print("The response of Client->get_combined_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_combined_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_pdf_id** | **str**| The combined PDF's ID. | 

### Return type

[**CombinedPdf**](CombinedPdf.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | combined PDF |  -  |
**404** | combined PDF not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_custom_file**
> CustomFile get_custom_file(custom_file_id)

Get a custom file

Returns a custom file, with a temporary URL to download it.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.custom_file import CustomFile
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    custom_file_id = 'custom_file_id_example' # str | The custom file's ID.

    try:
        # Get a custom file
        api_response = api_instance.get_custom_file(custom_file_id)
        print("The response of Client->get_custom_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_custom_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_id** | **str**| The custom file's ID. | 

### Return type

[**CustomFile**](CustomFile.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | custom file found |  -  |
**404** | custom file not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_folder**
> Folder get_folder(folder_id)

Get a folder

Returns a folder.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    folder_id = 'folder_id_example' # str | The folder's ID.

    try:
        # Get a folder
        api_response = api_instance.get_folder(folder_id)
        print("The response of Client->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The folder's ID. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | folder found |  -  |
**404** | folder not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_presign_url**
> UploadPresign get_presign_url()

Get a presigned URL to upload a file

Returns a presigned S3 form for uploading a file directly to DocSpring, for files too large to send in a
request body. POST the `fields` and the file (as `file`) to `url` as multipart/form-data, then pass
`fields.key` as the `cache_id` when you create a custom file.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.upload_presign import UploadPresign
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)

    try:
        # Get a presigned URL to upload a file
        api_response = api_instance.get_presign_url()
        print("The response of Client->get_presign_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_presign_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UploadPresign**](UploadPresign.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | presigned URL created |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_signature_request**
> SignatureRequest get_signature_request(signature_request_id)

Get a signature request

Returns a signature request, with the values the person has entered so far.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.signature_request import SignatureRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    signature_request_id = 'srq_1234567890abcdef01' # str | The signature request's ID.

    try:
        # Get a signature request
        api_response = api_instance.get_signature_request(signature_request_id)
        print("The response of Client->get_signature_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_signature_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request_id** | **str**| The signature request's ID. | 

### Return type

[**SignatureRequest**](SignatureRequest.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | signature request |  -  |
**404** | signature request not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_submission**
> Submission get_submission(submission_id)

Get a submission

Returns a submission, with its data and links to download its PDF.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | The submission's ID.

    try:
        # Get a submission
        api_response = api_instance.get_submission(submission_id)
        print("The response of Client->get_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| The submission's ID. | 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | processed submission |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_submission_batch**
> SubmissionBatch get_submission_batch(submission_batch_id, include_data=include_data)

Get a batch

Returns a batch with its submissions. The batch has finished once `processed_at` is set: its `state` is
`processed` when every PDF was generated, or `error` when any submission failed.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_batch import SubmissionBatch
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    submission_batch_id = 'sbb_1234567890abcdef05' # str | The batch's ID.
    include_data = true # bool | Include each submission's `data` (null without it). (optional)

    try:
        # Get a batch
        api_response = api_instance.get_submission_batch(submission_batch_id, include_data=include_data)
        print("The response of Client->get_submission_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_submission_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_batch_id** | **str**| The batch's ID. | 
 **include_data** | **bool**| Include each submission's `data` (null without it). | [optional] 

### Return type

[**SubmissionBatch**](SubmissionBatch.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | batch |  -  |
**404** | batch not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template**
> Template get_template(template_id, version=version)

Get a template

Returns a template: its draft, or one of its published versions.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    version = 'latest' # str | A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. (optional)

    try:
        # Get a template
        api_response = api_instance.get_template(template_id, version=version)
        print("The response of Client->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF template |  -  |
**404** | template not found |  -  |
**422** | invalid version |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template_diff**
> TemplateDiff get_template_diff(template_id, version=version)

Compare a version of a template with the one before it

Returns what changed in the template's draft since its latest published version (or in a published version
since the one before it): fields added, removed, changed and moved, the settings that changed, and whether
the document was replaced. Check it before you publish a version.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_diff import TemplateDiff
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    version = '0.1.0' # str | A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. (optional)

    try:
        # Compare a version of a template with the one before it
        api_response = api_instance.get_template_diff(template_id, version=version)
        print("The response of Client->get_template_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. | [optional] 

### Return type

[**TemplateDiff**](TemplateDiff.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the draft's changes since the latest published version |  -  |
**409** | the template's PDF hasn't been processed |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template_model_code**
> TemplateModelCode get_template_model_code(template_id, lang, version=version, just_types=just_types)

Generate typed code for a template's submission data

Generates types for a template's submission data in TypeScript, JavaScript, Ruby, Python, PHP, Java, C#,
Elixir, Go or Rust, so your app catches mistakes before it calls the API. `root_type_name` is the type of the
whole `data` object, and `just_types=true` leaves out the code that converts JSON to and from the types. Java
returns every class in `code`, each under a `// ClassName.java` comment. A template with no named fields
returns 422.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.model_code_language import ModelCodeLanguage
from docspring.models.template_model_code import TemplateModelCode
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    lang = docspring.ModelCodeLanguage() # ModelCodeLanguage | The language to generate the code in.
    version = 'draft' # str | The template version: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published), the version a submission uses by default. (optional)
    just_types = true # bool | Return only the types (interfaces, classes or structs), without the code that converts JSON to and from them. Default false. JavaScript has no types, PHP has no types-only code, and Rust's code is only types (serde converts the JSON), so theirs is the same either way. (optional)

    try:
        # Generate typed code for a template's submission data
        api_response = api_instance.get_template_model_code(template_id, lang, version=version, just_types=just_types)
        print("The response of Client->get_template_model_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template_model_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **lang** | [**ModelCodeLanguage**](.md)| The language to generate the code in. | 
 **version** | **str**| The template version: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published), the version a submission uses by default. | [optional] 
 **just_types** | **bool**| Return only the types (interfaces, classes or structs), without the code that converts JSON to and from them. Default false. JavaScript has no types, PHP has no types-only code, and Rust's code is only types (serde converts the JSON), so theirs is the same either way. | [optional] 

### Return type

[**TemplateModelCode**](TemplateModelCode.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | model code |  -  |
**422** | unknown language |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template_page_images**
> TemplatePageImages get_template_page_images(template_id, version=version)

Get images of a template's pages

Returns a JPEG image of each page of a PDF template's PDF, with temporary links to download them: the draft's
PDF, or a published version's. Use them to see the pages that fields are placed on.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_page_images import TemplatePageImages
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    version = 'latest' # str | A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. (optional)

    try:
        # Get images of a template's pages
        api_response = api_instance.get_template_page_images(template_id, version=version)
        print("The response of Client->get_template_page_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template_page_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. | [optional] 

### Return type

[**TemplatePageImages**](TemplatePageImages.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | page images |  -  |
**409** | no page images |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template_preview**
> TemplatePreview get_template_preview(template_id, preview_id)

Get a template preview

Returns a preview made with POST /templates/{template_id}/previews. Once it's `processed`, `pages` has a PNG
image of each page with a temporary link to download it: a preview has no PDF. Previews are deleted an hour
after they're created.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef02' # str | The template's ID.
    preview_id = 'tpv_1234567890abcdef0123' # str | The preview's ID.

    try:
        # Get a template preview
        api_response = api_instance.get_template_preview(template_id, preview_id)
        print("The response of Client->get_template_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **preview_id** | **str**| The preview's ID. | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | preview |  -  |
**404** | preview not found |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_template_schema**
> Dict[str, object] get_template_schema(template_id, version=version)

Get the JSON Schema of a template's submission data

Returns the JSON Schema that a submission's `data` must match. Use it to check data before you create
submissions, or to build a form for the template's fields.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    version = 'draft' # str | The template version: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published), the version a submission uses by default. (optional)

    try:
        # Get the JSON Schema of a template's submission data
        api_response = api_instance.get_template_schema(template_id, version=version)
        print("The response of Client->get_template_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_template_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| The template version: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published), the version a submission uses by default. | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template schema |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get a webhook

Returns a webhook.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.webhook import Webhook
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    webhook_id = 'webhook_id_example' # str | The webhook's ID.

    try:
        # Get a webhook
        api_response = api_instance.get_webhook(webhook_id)
        print("The response of Client->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook's ID. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | webhook found |  -  |
**404** | webhook not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_combined_pdfs**
> CombinedPdfList list_combined_pdfs(limit=limit, cursor=cursor)

List combined PDFs

Returns the combined PDFs in your account, newest first, one page at a time.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_pdf_list import CombinedPdfList
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)

    try:
        # List combined PDFs
        api_response = api_instance.list_combined_pdfs(limit=limit, cursor=cursor)
        print("The response of Client->list_combined_pdfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_combined_pdfs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 

### Return type

[**CombinedPdfList**](CombinedPdfList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | combined PDFs |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_custom_files**
> CustomFileList list_custom_files(limit=limit, cursor=cursor)

List custom files

Returns the custom files in your account, newest first, one page at a time.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.custom_file_list import CustomFileList
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)

    try:
        # List custom files
        api_response = api_instance.list_custom_files(limit=limit, cursor=cursor)
        print("The response of Client->list_custom_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_custom_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 

### Return type

[**CustomFileList**](CustomFileList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | custom files |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_folders**
> FolderList list_folders(parent_folder_id=parent_folder_id, limit=limit, cursor=cursor)

List folders

Returns the folders in your account, newest first, one page at a time. Pass `parent_folder_id` to list the
folders in one folder.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder_list import FolderList
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    parent_folder_id = 'fld_1234567890abcdef02' # str | Only list the folders in this folder. Without it, the list has every folder, at any depth. (optional)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'fld_1234567890abcdef02' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)

    try:
        # List folders
        api_response = api_instance.list_folders(parent_folder_id=parent_folder_id, limit=limit, cursor=cursor)
        print("The response of Client->list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_folder_id** | **str**| Only list the folders in this folder. Without it, the list has every folder, at any depth. | [optional] 
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 

### Return type

[**FolderList**](FolderList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | folders in a folder |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_submissions**
> SubmissionList list_submissions(template_id=template_id, test=test, created_after=created_after, created_before=created_before, include_data=include_data, limit=limit, cursor=cursor, state=state, include_files=include_files)

List submissions

Returns the submissions in your account, newest first, one page at a time. Each one is a summary: its `data`
is null unless you pass `include_data=true`, and its `files` are empty unless you pass `include_files=true`.
Get a submission by its ID for its signature requests, uploads and page images.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_list import SubmissionList
from docspring.models.submission_state import SubmissionState
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | Only list this template's submissions. (optional)
    test = false # bool | Only list test submissions (true) or live submissions (false). (optional)
    created_after = '2018-10-20T08:40:00Z' # datetime | Only list submissions created after this time (RFC 3339, such as `2025-01-31T09:00:00Z`). (optional)
    created_before = '2018-10-20T09:00:00Z' # datetime | Only list submissions created before this time. (optional)
    include_data = true # bool | Include each submission's `data` (null without it). (optional)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)
    state = docspring.SubmissionState() # SubmissionState | Only list submissions in this state (one state per request). The ones that failed are `invalid_data`, `error`, `syntax_error`, `image_download_failed` and `image_processing_failed`, and one still `pending` an hour after it was created is stuck. (optional)
    include_files = true # bool | Include each submission's generated files and their download links (`files`, empty without it), without the page images' links. (optional)

    try:
        # List submissions
        api_response = api_instance.list_submissions(template_id=template_id, test=test, created_after=created_after, created_before=created_before, include_data=include_data, limit=limit, cursor=cursor, state=state, include_files=include_files)
        print("The response of Client->list_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Only list this template's submissions. | [optional] 
 **test** | **bool**| Only list test submissions (true) or live submissions (false). | [optional] 
 **created_after** | **datetime**| Only list submissions created after this time (RFC 3339, such as `2025-01-31T09:00:00Z`). | [optional] 
 **created_before** | **datetime**| Only list submissions created before this time. | [optional] 
 **include_data** | **bool**| Include each submission's `data` (null without it). | [optional] 
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 
 **state** | [**SubmissionState**](.md)| Only list submissions in this state (one state per request). The ones that failed are `invalid_data`, `error`, `syntax_error`, `image_download_failed` and `image_processing_failed`, and one still `pending` an hour after it was created is stuck. | [optional] 
 **include_files** | **bool**| Include each submission's generated files and their download links (`files`, empty without it), without the page images' links. | [optional] 

### Return type

[**SubmissionList**](SubmissionList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | submissions |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_template_fields**
> TemplateFields list_template_fields(template_id, version=version)

List a template's fields

Returns a template's fields with all of their settings, page by page: the draft's fields, or a published
version's. A PDF template's fields are placed on its pages: GET /templates/{template_id}/page_images has images
of the pages.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_fields import TemplateFields
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    version = 'latest' # str | A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. (optional)

    try:
        # List a template's fields
        api_response = api_instance.list_template_fields(template_id, version=version)
        print("The response of Client->list_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **version** | **str**| A published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `draft`. | [optional] 

### Return type

[**TemplateFields**](TemplateFields.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fields |  -  |
**409** | the template's PDF hasn't been processed |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_template_submissions**
> SubmissionList list_template_submissions(template_id, test=test, created_after=created_after, created_before=created_before, include_data=include_data, limit=limit, cursor=cursor, state=state, include_files=include_files)

List a template's submissions

Returns a template's submissions (from every version of the template), newest first.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_list import SubmissionList
from docspring.models.submission_state import SubmissionState
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    test = True # bool | Only list test submissions (true) or live submissions (false). (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Only list submissions created after this time (RFC 3339, such as `2025-01-31T09:00:00Z`). (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | Only list submissions created before this time. (optional)
    include_data = True # bool | Include each submission's `data` (null without it). (optional)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)
    state = docspring.SubmissionState() # SubmissionState | Only list submissions in this state (one state per request). The ones that failed are `invalid_data`, `error`, `syntax_error`, `image_download_failed` and `image_processing_failed`, and one still `pending` an hour after it was created is stuck. (optional)
    include_files = True # bool | Include each submission's generated files and their download links (`files`, empty without it), without the page images' links. (optional)

    try:
        # List a template's submissions
        api_response = api_instance.list_template_submissions(template_id, test=test, created_after=created_after, created_before=created_before, include_data=include_data, limit=limit, cursor=cursor, state=state, include_files=include_files)
        print("The response of Client->list_template_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_template_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **test** | **bool**| Only list test submissions (true) or live submissions (false). | [optional] 
 **created_after** | **datetime**| Only list submissions created after this time (RFC 3339, such as `2025-01-31T09:00:00Z`). | [optional] 
 **created_before** | **datetime**| Only list submissions created before this time. | [optional] 
 **include_data** | **bool**| Include each submission's `data` (null without it). | [optional] 
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 
 **state** | [**SubmissionState**](.md)| Only list submissions in this state (one state per request). The ones that failed are `invalid_data`, `error`, `syntax_error`, `image_download_failed` and `image_processing_failed`, and one still `pending` an hour after it was created is stuck. | [optional] 
 **include_files** | **bool**| Include each submission's generated files and their download links (`files`, empty without it), without the page images' links. | [optional] 

### Return type

[**SubmissionList**](SubmissionList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template's submissions |  -  |
**404** | template not found |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_templates**
> TemplateSummaryList list_templates(query=query, parent_folder_id=parent_folder_id, limit=limit, cursor=cursor)

List templates

Returns the templates in your account (their drafts), newest first, one page at a time. Each one is a summary:
get a template by its ID for its settings, its PDF in full, its HTML, defaults and published versions.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_summary_list import TemplateSummaryList
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    query = 'rental' # str | Only list templates whose name contains this text (ignoring case). (optional)
    parent_folder_id = 'fld_1234567890abcdef01' # str | Only list the templates in this folder (not in its subfolders). (optional)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)

    try:
        # List templates
        api_response = api_instance.list_templates(query=query, parent_folder_id=parent_folder_id, limit=limit, cursor=cursor)
        print("The response of Client->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Only list templates whose name contains this text (ignoring case). | [optional] 
 **parent_folder_id** | **str**| Only list the templates in this folder (not in its subfolders). | [optional] 
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 

### Return type

[**TemplateSummaryList**](TemplateSummaryList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | templates |  -  |
**422** | invalid query parameters |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookList list_webhooks(event_type=event_type, mode=mode, template_id=template_id, folder_id=folder_id, api_token_id=api_token_id, limit=limit, cursor=cursor)

List webhooks

Returns the webhooks in your account, newest first, one page at a time. Filter them by event type, mode, or
the API token, template or folder they're scoped to.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.webhook_event_type import WebhookEventType
from docspring.models.webhook_list import WebhookList
from docspring.models.webhook_mode import WebhookMode
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    event_type = docspring.WebhookEventType() # WebhookEventType | Only list webhooks that subscribe to this event. (optional)
    mode = docspring.WebhookMode() # WebhookMode | Only list webhooks set to this mode. (optional)
    template_id = 'tpl_1234567890abcdef01' # str | Only list webhooks scoped to this template. (optional)
    folder_id = 'folder_id_example' # str | Only list webhooks scoped to this folder. (optional)
    api_token_id = 'api_token_id_example' # str | Only list webhooks scoped to this API token. (optional)
    limit = 50 # int | How many items to return (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. (optional)

    try:
        # List webhooks
        api_response = api_instance.list_webhooks(event_type=event_type, mode=mode, template_id=template_id, folder_id=folder_id, api_token_id=api_token_id, limit=limit, cursor=cursor)
        print("The response of Client->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | [**WebhookEventType**](.md)| Only list webhooks that subscribe to this event. | [optional] 
 **mode** | [**WebhookMode**](.md)| Only list webhooks set to this mode. | [optional] 
 **template_id** | **str**| Only list webhooks scoped to this template. | [optional] 
 **folder_id** | **str**| Only list webhooks scoped to this folder. | [optional] 
 **api_token_id** | **str**| Only list webhooks scoped to this API token. | [optional] 
 **limit** | **int**| How many items to return (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| The previous page's `next_cursor`, to get the next page. It's the ID of that page's last item, so get the next page before you delete or change the items on this one. | [optional] 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | webhooks for a template and event |  -  |
**422** | unknown event type |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **move_folder**
> Folder move_folder(folder_id, body)

Move a folder

Moves a folder into another folder, or to the root with `parent_folder_id: null`. Its templates and folders
move with it. A folder can't move into itself or one of its own folders.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.models.move_folder_request import MoveFolderRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    folder_id = 'folder_id_example' # str | The folder's ID.
    body = {"parent_folder_id":"fld_1234567890abcdef02"} # MoveFolderRequest | Where to move the folder.

    try:
        # Move a folder
        api_response = api_instance.move_folder(folder_id, body)
        print("The response of Client->move_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->move_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The folder's ID. | 
 **body** | [**MoveFolderRequest**](MoveFolderRequest.md)| Where to move the folder. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | folder moved into another folder |  -  |
**422** | invalid move |  -  |
**404** | folder not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **move_template**
> Template move_template(template_id, body)

Move a template to a folder

Moves a template and all of its published versions to a folder, or to the root (`null`).

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.move_template_request import MoveTemplateRequest
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"parent_folder_id":null} # MoveTemplateRequest | Where to move the template.

    try:
        # Move a template to a folder
        api_response = api_instance.move_template(template_id, body)
        print("The response of Client->move_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->move_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**MoveTemplateRequest**](MoveTemplateRequest.md)| Where to move the template. | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template moved |  -  |
**422** | invalid move |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **publish_template_version**
> TemplateVersion publish_template_version(template_id, body)

Publish a template version

Publishes the template's draft as a new version. Its content (the PDF or HTML, fields, name and description)
never changes, while settings such as `webhook_url` and `public_submissions` keep following the draft.
`version_type` says which part of the latest version number goes up. While the template's PDF is downloading
or being processed, or DocSpring is setting up its fields, it returns a 409 that says so.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.publish_template_version_request import PublishTemplateVersionRequest
from docspring.models.template_version import TemplateVersion
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"version_type":"minor","description":"Added the signature fields"} # PublishTemplateVersionRequest | The version to publish.

    try:
        # Publish a template version
        api_response = api_instance.publish_template_version(template_id, body)
        print("The response of Client->publish_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->publish_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**PublishTemplateVersionRequest**](PublishTemplateVersionRequest.md)| The version to publish. | 

### Return type

[**TemplateVersion**](TemplateVersion.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | version published |  -  |
**422** | invalid version type |  -  |
**404** | template not found |  -  |
**409** | no changes to publish |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **remove_template_fields**
> TemplateFields remove_template_fields(template_id, body)

Remove fields from a template

Removes fields from a template's draft and returns the fields that are left. Conditional logic that used only
the removed fields is removed too.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.remove_template_fields_request import RemoveTemplateFieldsRequest
from docspring.models.template_fields import TemplateFields
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"field_ids":[3]} # RemoveTemplateFieldsRequest | The fields to remove from the template's draft.

    try:
        # Remove fields from a template
        api_response = api_instance.remove_template_fields(template_id, body)
        print("The response of Client->remove_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->remove_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**RemoveTemplateFieldsRequest**](RemoveTemplateFieldsRequest.md)| The fields to remove from the template's draft. | 

### Return type

[**TemplateFields**](TemplateFields.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fields removed |  -  |
**422** | a field the template does not have |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **rename_folder**
> Folder rename_folder(folder_id, body)

Rename a folder

Renames a folder. The name must be unique within its parent folder.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.models.rename_folder_request import RenameFolderRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    folder_id = 'folder_id_example' # str | The folder's ID.
    body = {"name":"Folder 3"} # RenameFolderRequest | The folder's new name.

    try:
        # Rename a folder
        api_response = api_instance.rename_folder(folder_id, body)
        print("The response of Client->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->rename_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The folder's ID. | 
 **body** | [**RenameFolderRequest**](RenameFolderRequest.md)| The folder's new name. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | folder renamed |  -  |
**422** | name already exists |  -  |
**404** | folder not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **reorder_template_fields**
> TemplateFields reorder_template_fields(template_id, body)

Reorder a template's fields

Changes the order of the fields in a template's draft and returns them in their new order. Send every field's
ID: each field stays on its page, and a page's fields are printed in this order, so a later field prints over
an earlier one where they overlap. Their values are in this order in the template's data schema and forms.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.reorder_template_fields_request import ReorderTemplateFieldsRequest
from docspring.models.template_fields import TemplateFields
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"field_ids":[3,1,2]} # ReorderTemplateFieldsRequest | The new order of the fields in the template's draft.

    try:
        # Reorder a template's fields
        api_response = api_instance.reorder_template_fields(template_id, body)
        print("The response of Client->reorder_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->reorder_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**ReorderTemplateFieldsRequest**](ReorderTemplateFieldsRequest.md)| The new order of the fields in the template's draft. | 

### Return type

[**TemplateFields**](TemplateFields.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fields reordered |  -  |
**422** | a field missing from the order |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **restore_template_version**
> Template restore_template_version(template_id, body)

Restore a template version

Replaces the template's draft with a copy of one of its published versions. The draft keeps its settings that apply to every version, such as `webhook_url`.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.restore_template_version_request import RestoreTemplateVersionRequest
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"version":"0.1.0"} # RestoreTemplateVersionRequest | The version to restore.

    try:
        # Restore a template version
        api_response = api_instance.restore_template_version(template_id, body)
        print("The response of Client->restore_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->restore_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**RestoreTemplateVersionRequest**](RestoreTemplateVersionRequest.md)| The version to restore. | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | version restored |  -  |
**409** | template is locked |  -  |
**422** | unknown version |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **test_authentication**
> AuthenticationCheck test_authentication()

Test authentication

Checks whether your API token is valid by making an authenticated request. This endpoint is useful for
verifying credentials during setup or troubleshooting issues.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.authentication_check import AuthenticationCheck
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)

    try:
        # Test authentication
        api_response = api_instance.test_authentication()
        print("The response of Client->test_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->test_authentication: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticationCheck**](AuthenticationCheck.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | authentication succeeded |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **update_signature_request**
> SignatureRequest update_signature_request(signature_request_id, body)

Update a signature request

Changes a pending signature request's metadata, or how your app authenticated the person (for the audit trail).
Once the person has opened it, only its metadata can be changed, and a completed or declined signature
request can't be changed.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.signature_request import SignatureRequest
from docspring.models.update_signature_request_request import UpdateSignatureRequestRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    signature_request_id = 'srq_1234567890abcdef01' # str | The signature request's ID.
    body = {"metadata":{"user_id":43},"auth_type":"oauth","auth_provider":"google","auth_session_started_at":"2018-10-20T08:00:00Z","auth_user_id_hash":"8ae0e445664ca53407906db8638d8ba07a2383f656383a4427bed1ab645ca29a"} # UpdateSignatureRequestRequest | The settings to change. Properties left out keep their values.

    try:
        # Update a signature request
        api_response = api_instance.update_signature_request(signature_request_id, body)
        print("The response of Client->update_signature_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->update_signature_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_request_id** | **str**| The signature request's ID. | 
 **body** | [**UpdateSignatureRequestRequest**](UpdateSignatureRequestRequest.md)| The settings to change. Properties left out keep their values. | 

### Return type

[**SignatureRequest**](SignatureRequest.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | signature request updated |  -  |
**409** | signature request completed |  -  |
**422** | invalid request |  -  |
**404** | signature request not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **update_template**
> Template update_template(template_id, body)

Update a template

Changes a template's draft. Properties left out keep their values. `defaults` and `html_engine_options`
replace the whole object, and `field_groups` changes only the groups it lists. Settings such as
`webhook_url`, `public_submissions` and `expire_after` apply to every published version too, and setting
`parent_folder_id` moves the template and all of its published versions.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.models.update_template_request import UpdateTemplateRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"name":"Rental Contract 2025","parent_folder_id":null,"slack_webhook_url":"https://hooks.slack.com/services/T000/B000/XXXX","encrypt_pdfs_password":null,"default_form_mode":"dual","ai_field_naming_language":"form_language","defaults":{"typeface":"Helvetica","font_size":10,"bold":true}} # UpdateTemplateRequest | The settings to change. Properties left out keep their values.

    try:
        # Update a template
        api_response = api_instance.update_template(template_id, body)
        print("The response of Client->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)| The settings to change. Properties left out keep their values. | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template updated |  -  |
**409** | template is locked |  -  |
**422** | invalid field group changes |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **update_template_document**
> Template update_template_document(template_id, body, wait=wait)

Replace a template's document

Replaces a PDF template's PDF, or a Word template's Word document (from a .docx or an .odt), with one you
uploaded with the presigned upload (GET /uploads/presign) (`cache_id`), a link to download it from
(`document_url`), or the file in base64 (`document_base64`). A PDF template's fields stay where they are,
unless `reimport_fields` replaces them with the new PDF's fillable fields, and a Word template gets a field
for each new tag. To send the file as `multipart/form-data` instead, use PUT
/templates/{template_id}/document/upload.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.models.update_template_document_request import UpdateTemplateDocumentRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"cache_id":"cache/original-0000000000","filename":"fw8ben.pdf","reimport_fields":true} # UpdateTemplateDocumentRequest | The new PDF, or a Word template's new Word document, as one of `cache_id`, `document_url` and `document_base64`.
    wait = True # bool | Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. (optional)

    try:
        # Replace a template's document
        api_response = api_instance.update_template_document(template_id, body, wait=wait)
        print("The response of Client->update_template_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->update_template_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**UpdateTemplateDocumentRequest**](UpdateTemplateDocumentRequest.md)| The new PDF, or a Word template's new Word document, as one of `cache_id`, `document_url` and `document_base64`. | 
 **wait** | **bool**| Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF replaced |  -  |
**409** | template is locked, so its fields can't be re-imported |  -  |
**422** | no document, or more than one |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's template_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **update_template_fields**
> TemplateFields update_template_fields(template_id, body)

Update a template's fields

Changes fields of a template's draft and returns all of its fields. Settings left out keep their values. A
shared setting (`type`, `required`, `default`, ...) changes for every field with the same name.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_fields import TemplateFields
from docspring.models.update_template_fields_request import UpdateTemplateFieldsRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"fields":[{"id":0,"x":5}]} # UpdateTemplateFieldsRequest | The fields to change in the template's draft.

    try:
        # Update a template's fields
        api_response = api_instance.update_template_fields(template_id, body)
        print("The response of Client->update_template_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->update_template_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**UpdateTemplateFieldsRequest**](UpdateTemplateFieldsRequest.md)| The fields to change in the template's draft. | 

### Return type

[**TemplateFields**](TemplateFields.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fields updated |  -  |
**422** | invalid changes |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(webhook_id, body)

Update a webhook

Updates a webhook. Only the properties you send change.

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.update_webhook_request import UpdateWebhookRequest
from docspring.models.webhook import Webhook
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    webhook_id = 'webhook_id_example' # str | The webhook's ID.
    body = {"name":"Updated Webhook","enabled":false} # UpdateWebhookRequest | The settings to change. Properties left out keep their values.

    try:
        # Update a webhook
        api_response = api_instance.update_webhook(webhook_id, body)
        print("The response of Client->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook's ID. | 
 **body** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)| The settings to change. Properties left out keep their values. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | webhook updated |  -  |
**403** | turning the webhook on would go over the plan's integration limit |  -  |
**404** | webhook not found |  -  |
**422** | invalid webhook |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **upload_template**
> Template upload_template(document, wait=wait, name=name, description=description, parent_folder_id=parent_folder_id, ai_field_naming_language=ai_field_naming_language, detect_fields=detect_fields, field_source=field_source, field_naming=field_naming, field_logic=field_logic, output_format=output_format)

Create a template from an uploaded PDF or Word document

Creates a PDF template from a PDF, or a Word template from a Word document (.docx) or an OpenDocument text
file (.odt), sent with the request (`multipart/form-data`). A Word template needs its `output_format`. For
large files, upload the file with the presigned upload (GET /uploads/presign) and create the template with
POST /templates.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    document = None # bytes | A PDF (for a PDF template) or a Word document (.docx or .odt, for a Word template). DocSpring converts an OpenDocument text file (.odt) to a Word document after responding: the template's `document.state` is `converting` until then (sync.api hosts wait for it).
    wait = True # bool | Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. (optional)
    name = 'name_example' # str | The template's name. (optional)
    description = 'description_example' # str | The template's description. (optional)
    parent_folder_id = 'parent_folder_id_example' # str | The folder to put the template in. Left out, it's created at the root. (optional)
    ai_field_naming_language = docspring.AiFieldNamingLanguage() # AiFieldNamingLanguage | The language AI field setup names fields in: `auto` uses the form's language when it's written in the Latin alphabet without accents, and English otherwise; `english` always uses English; `form_language` uses the form's language and script. Default: your account's template settings. (optional)
    detect_fields = True # bool | Set up the PDF's fields as DocSpring's "Automatically detect fields" upload option does: import or detect the fields, name them with AI, and set up conditional logic. `field_source`, `field_naming` and `field_logic` choose how. Default false. `document.page_processing_statuses` and `document.field_logic_status` show how it's going, and `document.state` becomes `processed` once every page's fields are set up. (optional)
    field_source = docspring.FieldSetupSource() # FieldSetupSource | With `detect_fields`, where the fields come from. `auto` (the default) imports the form fields of a fillable PDF and detects the fields of a PDF without them; `pdf_detection` detects the fields from the page layout, even on a fillable PDF; `pdf_form_fields` only imports the PDF's form fields. (optional)
    field_naming = docspring.FieldSetupNaming() # FieldSetupNaming | With `detect_fields`, how the fields are named. `ai` (the default) names them and sets their types and settings with AI; `preserve` keeps the names of the PDF's form fields, and AI only names the fields it detected. `preserve` needs `field_source` `auto` or `pdf_form_fields`. (optional)
    field_logic = docspring.FieldSetupLogic() # FieldSetupLogic | With `detect_fields`, whether AI reads the whole form once the fields are named and sets up conditional logic and required fields (`ai`) or not (`none`). Default: your account's template settings. (optional)
    output_format = docspring.OutputFormat() # OutputFormat | What each submission of a Word template makes unless its request sets `output_formats`: `docx` (a Word document), `odt` (an OpenDocument file, converted from the Word document) or `pdf`. Required when `document` is a Word document. (optional)

    try:
        # Create a template from an uploaded PDF or Word document
        api_response = api_instance.upload_template(document, wait=wait, name=name, description=description, parent_folder_id=parent_folder_id, ai_field_naming_language=ai_field_naming_language, detect_fields=detect_fields, field_source=field_source, field_naming=field_naming, field_logic=field_logic, output_format=output_format)
        print("The response of Client->upload_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->upload_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **bytes**| A PDF (for a PDF template) or a Word document (.docx or .odt, for a Word template). DocSpring converts an OpenDocument text file (.odt) to a Word document after responding: the template's `document.state` is `converting` until then (sync.api hosts wait for it). | 
 **wait** | **bool**| Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. | [optional] 
 **name** | **str**| The template's name. | [optional] 
 **description** | **str**| The template's description. | [optional] 
 **parent_folder_id** | **str**| The folder to put the template in. Left out, it's created at the root. | [optional] 
 **ai_field_naming_language** | [**AiFieldNamingLanguage**](AiFieldNamingLanguage.md)| The language AI field setup names fields in: `auto` uses the form's language when it's written in the Latin alphabet without accents, and English otherwise; `english` always uses English; `form_language` uses the form's language and script. Default: your account's template settings. | [optional] 
 **detect_fields** | **bool**| Set up the PDF's fields as DocSpring's "Automatically detect fields" upload option does: import or detect the fields, name them with AI, and set up conditional logic. `field_source`, `field_naming` and `field_logic` choose how. Default false. `document.page_processing_statuses` and `document.field_logic_status` show how it's going, and `document.state` becomes `processed` once every page's fields are set up. | [optional] 
 **field_source** | [**FieldSetupSource**](FieldSetupSource.md)| With `detect_fields`, where the fields come from. `auto` (the default) imports the form fields of a fillable PDF and detects the fields of a PDF without them; `pdf_detection` detects the fields from the page layout, even on a fillable PDF; `pdf_form_fields` only imports the PDF's form fields. | [optional] 
 **field_naming** | [**FieldSetupNaming**](FieldSetupNaming.md)| With `detect_fields`, how the fields are named. `ai` (the default) names them and sets their types and settings with AI; `preserve` keeps the names of the PDF's form fields, and AI only names the fields it detected. `preserve` needs `field_source` `auto` or `pdf_form_fields`. | [optional] 
 **field_logic** | [**FieldSetupLogic**](FieldSetupLogic.md)| With `detect_fields`, whether AI reads the whole form once the fields are named and sets up conditional logic and required fields (`ai`) or not (`none`). Default: your account's template settings. | [optional] 
 **output_format** | [**OutputFormat**](OutputFormat.md)| What each submission of a Word template makes unless its request sets `output_formats`: `docx` (a Word document), `odt` (an OpenDocument file, converted from the Word document) or `pdf`. Required when `document` is a Word document. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PDF template created |  -  |
**422** | invalid upload |  -  |
**403** | the plan's template limit is reached |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's template_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **upload_template_document**
> Template upload_template_document(template_id, document, wait=wait, reimport_fields=reimport_fields)

Replace a template's document with an uploaded file

Replaces a PDF template's PDF, or a Word template's Word document, with one sent with the request
(`multipart/form-data`). A PDF template's fields stay where they are, unless `reimport_fields` replaces them
with the new PDF's fillable fields, and a Word template gets a field for each new tag.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    document = None # bytes | The new PDF, or the new Word document (.docx or .odt) of a Word template.
    wait = True # bool | Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. (optional)
    reimport_fields = True # bool | Replace all of the template's fields with the fillable fields in the new PDF, once DocSpring has processed it (`document.field_reimport_state`). As on a first upload, the default typeface, font size, bold and color are taken from the PDF's fields; the template's other settings are kept. If the PDF has no fillable fields, the template keeps its fields. A locked template can't re-import its fields. Only for PDF templates: a Word template adds a field for each new tag. (optional)

    try:
        # Replace a template's document with an uploaded file
        api_response = api_instance.upload_template_document(template_id, document, wait=wait, reimport_fields=reimport_fields)
        print("The response of Client->upload_template_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->upload_template_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **document** | **bytes**| The new PDF, or the new Word document (.docx or .odt) of a Word template. | 
 **wait** | **bool**| Wait until the PDF has been processed, a `document_url`'s PDF or Word document downloaded, and an OpenDocument file converted, before responding. Default true on sync.api hosts. | [optional] 
 **reimport_fields** | **bool**| Replace all of the template's fields with the fillable fields in the new PDF, once DocSpring has processed it (`document.field_reimport_state`). As on a first upload, the default typeface, font size, bold and color are taken from the PDF's fields; the template's other settings are kept. If the PDF has no fillable fields, the template keeps its fields. A locked template can't re-import its fields. Only for PDF templates: a Word template adds a field for each new tag. | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF replaced |  -  |
**422** | an HTML template |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |
**504** | On a sync.api host, the wait ran out: the record was saved and is still being processed. Get it by the ID in the error's template_id instead of sending the request again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

# **validate_submission**
> SubmissionValidation validate_submission(template_id, body, version=version)

Check a submission without creating it

Checks a submission as creating it would (its data against the template's fields, its settings and signature
requests) without saving it, generating anything or using credits. It doesn't check your account's credits.
The response says whether the submission is valid, and if not, has the error that creating it would return.


### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_validation import SubmissionValidation
from docspring.models.validate_submission_request import ValidateSubmissionRequest
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with docspring.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspring.Client(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | The template's ID.
    body = {"data":{"first_name":"John","last_name":"Smith","phone_number":"+11234567890"}} # ValidateSubmissionRequest | The submission's data and settings.
    version = 'latest' # str | The template version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). (optional)

    try:
        # Check a submission without creating it
        api_response = api_instance.validate_submission(template_id, body, version=version)
        print("The response of Client->validate_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Client->validate_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template's ID. | 
 **body** | [**ValidateSubmissionRequest**](ValidateSubmissionRequest.md)| The submission's data and settings. | 
 **version** | **str**| The template version to use: a published version (`1.2.0`, or `1` for the latest 1.x.x), `latest` or `draft`. Default `latest` (the draft when no version has been published). | [optional] 

### Return type

[**SubmissionValidation**](SubmissionValidation.md)

### Authorization

[api_token_basic](../README.md#install-and-configure)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | valid submission |  -  |
**404** | template not found |  -  |
**422** | invalid request |  -  |
**401** | authentication failed |  -  |
**429** | Too many requests: wait the number of seconds in the Retry-After header, then send the request again. |  * Retry-After - Seconds until you can send the request again. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#methods) [[Back to Model list]](../README.md#methods) [[Back to README]](../README.md)

