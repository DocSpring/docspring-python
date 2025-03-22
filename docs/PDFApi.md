# docspring.PDFApi

All URIs are relative to *https://sync.api.docspring.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fields_to_template**](PDFApi.md#add_fields_to_template) | **PUT** /templates/{template_id}/add_fields | Add new fields to a Template
[**batch_generate_pdfs**](PDFApi.md#batch_generate_pdfs) | **POST** /submissions/batches | Generates multiple PDFs
[**combine_pdfs**](PDFApi.md#combine_pdfs) | **POST** /combined_submissions?v&#x3D;2 | Merge submission PDFs, template PDFs, or custom files
[**combine_submissions**](PDFApi.md#combine_submissions) | **POST** /combined_submissions | Merge generated PDFs together
[**copy_template**](PDFApi.md#copy_template) | **POST** /templates/{template_id}/copy | Copy a Template
[**create_custom_file_from_upload**](PDFApi.md#create_custom_file_from_upload) | **POST** /custom_files | Create a new custom file from a cached presign upload
[**create_data_request_event**](PDFApi.md#create_data_request_event) | **POST** /data_requests/{data_request_id}/events | Creates a new event for emailing a signee a request for signature
[**create_data_request_token**](PDFApi.md#create_data_request_token) | **POST** /data_requests/{data_request_id}/tokens | Creates a new data request token for form authentication
[**create_folder**](PDFApi.md#create_folder) | **POST** /folders/ | Create a folder
[**create_html_template**](PDFApi.md#create_html_template) | **POST** /templates?endpoint_description&#x3D;html | Create a new HTML template
[**create_pdf_template**](PDFApi.md#create_pdf_template) | **POST** /templates | Create a new PDF template with a form POST file upload
[**create_pdf_template_from_upload**](PDFApi.md#create_pdf_template_from_upload) | **POST** /templates?endpoint_description&#x3D;cached_upload | Create a new PDF template from a cached presign upload
[**delete_folder**](PDFApi.md#delete_folder) | **DELETE** /folders/{folder_id} | Delete a folder
[**delete_template**](PDFApi.md#delete_template) | **DELETE** /templates/{template_id} | Delete a template
[**expire_combined_submission**](PDFApi.md#expire_combined_submission) | **DELETE** /combined_submissions/{combined_submission_id} | Expire a combined submission
[**expire_submission**](PDFApi.md#expire_submission) | **DELETE** /submissions/{submission_id} | Expire a PDF submission
[**generate_pdf**](PDFApi.md#generate_pdf) | **POST** /templates/{template_id}/submissions | Generates a new PDF
[**generate_pdf_for_html_template**](PDFApi.md#generate_pdf_for_html_template) | **POST** /templates/{template_id}/submissions?endpoint_description&#x3D;html_templates | Generates a new PDF for an HTML template
[**generate_preview**](PDFApi.md#generate_preview) | **POST** /submissions/{submission_id}/generate_preview | Generated a preview PDF for partially completed data requests
[**get_combined_submission**](PDFApi.md#get_combined_submission) | **GET** /combined_submissions/{combined_submission_id} | Check the status of a combined submission (merged PDFs)
[**get_data_request**](PDFApi.md#get_data_request) | **GET** /data_requests/{data_request_id} | Look up a submission data request
[**get_full_template**](PDFApi.md#get_full_template) | **GET** /templates/{template_id}?full&#x3D;true | Fetch the full attributes for a PDF template
[**get_presign_url**](PDFApi.md#get_presign_url) | **GET** /uploads/presign | Get a presigned URL so that you can upload a file to our AWS S3 bucket
[**get_submission**](PDFApi.md#get_submission) | **GET** /submissions/{submission_id} | Check the status of a PDF
[**get_submission_batch**](PDFApi.md#get_submission_batch) | **GET** /submissions/batches/{submission_batch_id} | Check the status of a submission batch job
[**get_template**](PDFApi.md#get_template) | **GET** /templates/{template_id} | Check the status of an uploaded template
[**get_template_schema**](PDFApi.md#get_template_schema) | **GET** /templates/{template_id}/schema | Fetch the JSON schema for a template
[**list_combined_submissions**](PDFApi.md#list_combined_submissions) | **GET** /combined_submissions | Get a list of all combined submissions
[**list_folders**](PDFApi.md#list_folders) | **GET** /folders/ | Get a list of all folders
[**list_submissions**](PDFApi.md#list_submissions) | **GET** /submissions | List all submissions
[**list_template_submissions**](PDFApi.md#list_template_submissions) | **GET** /templates/{template_id}/submissions | List all submissions for a given template
[**list_templates**](PDFApi.md#list_templates) | **GET** /templates | Get a list of all templates
[**move_folder_to_folder**](PDFApi.md#move_folder_to_folder) | **POST** /folders/{folder_id}/move | Move a folder
[**move_template_to_folder**](PDFApi.md#move_template_to_folder) | **POST** /templates/{template_id}/move | Move Template to folder
[**publish_template_version**](PDFApi.md#publish_template_version) | **POST** /templates/{template_id}/publish_version | Publish a template version
[**rename_folder**](PDFApi.md#rename_folder) | **POST** /folders/{folder_id}/rename | Rename a folder
[**restore_template_version**](PDFApi.md#restore_template_version) | **POST** /templates/{template_id}/restore_version | Restore a template version
[**test_authentication**](PDFApi.md#test_authentication) | **GET** /authentication | Test Authentication
[**update_data_request**](PDFApi.md#update_data_request) | **PUT** /data_requests/{data_request_id} | Update a submission data request
[**update_template**](PDFApi.md#update_template) | **PUT** /templates/{template_id} | Update a Template


# **add_fields_to_template**
> TemplateAddFieldsResponse add_fields_to_template(template_id, data)

Add new fields to a Template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.add_fields_data import AddFieldsData
from docspring.models.template_add_fields_response import TemplateAddFieldsResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef02' # str | 
    data = docspring.AddFieldsData() # AddFieldsData | 

    try:
        # Add new fields to a Template
        api_response = api_instance.add_fields_to_template(template_id, data)
        print("The response of PDFApi->add_fields_to_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->add_fields_to_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **data** | [**AddFieldsData**](AddFieldsData.md)|  | 

### Return type

[**TemplateAddFieldsResponse**](TemplateAddFieldsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | add fields success |  -  |
**422** | add fields error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_generate_pdfs**
> BatchGeneratePdfs201Response batch_generate_pdfs(data, wait=wait)

Generates multiple PDFs

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.batch_generate_pdfs201_response import BatchGeneratePdfs201Response
from docspring.models.submission_batch_data import SubmissionBatchData
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.SubmissionBatchData() # SubmissionBatchData | 
    wait = True # bool | Wait for submission batch to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) (optional) (default to True)

    try:
        # Generates multiple PDFs
        api_response = api_instance.batch_generate_pdfs(data, wait=wait)
        print("The response of PDFApi->batch_generate_pdfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->batch_generate_pdfs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubmissionBatchData**](SubmissionBatchData.md)|  | 
 **wait** | **bool**| Wait for submission batch to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) | [optional] [default to True]

### Return type

[**BatchGeneratePdfs201Response**](BatchGeneratePdfs201Response.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | submissions created |  -  |
**200** | some PDFs with invalid data |  -  |
**401** | authentication failed |  -  |
**422** | array of arrays |  -  |
**400** | invalid JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_pdfs**
> CreateCombinedSubmissionResponse combine_pdfs(data)

Merge submission PDFs, template PDFs, or custom files

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combine_pdfs_data import CombinePdfsData
from docspring.models.create_combined_submission_response import CreateCombinedSubmissionResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CombinePdfsData() # CombinePdfsData | 

    try:
        # Merge submission PDFs, template PDFs, or custom files
        api_response = api_instance.combine_pdfs(data)
        print("The response of PDFApi->combine_pdfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->combine_pdfs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CombinePdfsData**](CombinePdfsData.md)|  | 

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | combined submission created |  -  |
**422** | invalid request |  -  |
**400** | invalid JSON |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_submissions**
> CreateCombinedSubmissionResponse combine_submissions(data, wait=wait)

Merge generated PDFs together

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_submission_data import CombinedSubmissionData
from docspring.models.create_combined_submission_response import CreateCombinedSubmissionResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CombinedSubmissionData() # CombinedSubmissionData | 
    wait = True # bool | Wait for combined submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) (optional) (default to True)

    try:
        # Merge generated PDFs together
        api_response = api_instance.combine_submissions(data, wait=wait)
        print("The response of PDFApi->combine_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->combine_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CombinedSubmissionData**](CombinedSubmissionData.md)|  | 
 **wait** | **bool**| Wait for combined submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) | [optional] [default to True]

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | combined submission created |  -  |
**422** | invalid request |  -  |
**400** | invalid JSON |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_template**
> TemplatePreview copy_template(template_id, options=options)

Copy a Template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.copy_template_options import CopyTemplateOptions
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    options = docspring.CopyTemplateOptions() # CopyTemplateOptions |  (optional)

    try:
        # Copy a Template
        api_response = api_instance.copy_template(template_id, options=options)
        print("The response of PDFApi->copy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->copy_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **options** | [**CopyTemplateOptions**](CopyTemplateOptions.md)|  | [optional] 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | copy template success |  -  |
**404** | folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_file_from_upload**
> CreateCustomFileResponse create_custom_file_from_upload(data)

Create a new custom file from a cached presign upload

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_custom_file_data import CreateCustomFileData
from docspring.models.create_custom_file_response import CreateCustomFileResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CreateCustomFileData() # CreateCustomFileData | 

    try:
        # Create a new custom file from a cached presign upload
        api_response = api_instance.create_custom_file_from_upload(data)
        print("The response of PDFApi->create_custom_file_from_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_custom_file_from_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateCustomFileData**](CreateCustomFileData.md)|  | 

### Return type

[**CreateCustomFileResponse**](CreateCustomFileResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns the custom file |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_request_event**
> CreateSubmissionDataRequestEventResponse create_data_request_event(data_request_id, event)

Creates a new event for emailing a signee a request for signature

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_submission_data_request_event_request import CreateSubmissionDataRequestEventRequest
from docspring.models.create_submission_data_request_event_response import CreateSubmissionDataRequestEventResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data_request_id = 'drq_1234567890abcdef01' # str | 
    event = docspring.CreateSubmissionDataRequestEventRequest() # CreateSubmissionDataRequestEventRequest | 

    try:
        # Creates a new event for emailing a signee a request for signature
        api_response = api_instance.create_data_request_event(data_request_id, event)
        print("The response of PDFApi->create_data_request_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_data_request_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 
 **event** | [**CreateSubmissionDataRequestEventRequest**](CreateSubmissionDataRequestEventRequest.md)|  | 

### Return type

[**CreateSubmissionDataRequestEventResponse**](CreateSubmissionDataRequestEventResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | event created |  -  |
**401** | authentication failed |  -  |
**422** | message recipient must not be blank |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_request_token**
> CreateSubmissionDataRequestTokenResponse create_data_request_token(data_request_id, type=type)

Creates a new data request token for form authentication

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_submission_data_request_token_response import CreateSubmissionDataRequestTokenResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data_request_id = 'drq_1234567890abcdef01' # str | 
    type = 'api' # str |  (optional)

    try:
        # Creates a new data request token for form authentication
        api_response = api_instance.create_data_request_token(data_request_id, type=type)
        print("The response of PDFApi->create_data_request_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_data_request_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 
 **type** | **str**|  | [optional] 

### Return type

[**CreateSubmissionDataRequestTokenResponse**](CreateSubmissionDataRequestTokenResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | token created |  -  |
**401** | authentication failed |  -  |
**422** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(data)

Create a folder

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_folder_data import CreateFolderData
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CreateFolderData() # CreateFolderData | 

    try:
        # Create a folder
        api_response = api_instance.create_folder(data)
        print("The response of PDFApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateFolderData**](CreateFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | name already exist |  -  |
**404** | parent folder doesn&#39;t exist |  -  |
**200** | folder created inside another folder |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_template**
> TemplatePreview create_html_template(data)

Create a new HTML template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_html_template import CreateHtmlTemplate
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CreateHtmlTemplate() # CreateHtmlTemplate | 

    try:
        # Create a new HTML template
        api_response = api_instance.create_html_template(data)
        print("The response of PDFApi->create_html_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_html_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateHtmlTemplate**](CreateHtmlTemplate.md)|  | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns a created template |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pdf_template**
> TemplatePreview create_pdf_template(template_document, template_name, wait=wait, template_description=template_description, template_parent_folder_id=template_parent_folder_id)

Create a new PDF template with a form POST file upload

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_document = None # bytearray | 
    template_name = 'template_name_example' # str | 
    wait = True # bool | Wait for template document to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) (optional) (default to True)
    template_description = 'template_description_example' # str |  (optional)
    template_parent_folder_id = 'template_parent_folder_id_example' # str |  (optional)

    try:
        # Create a new PDF template with a form POST file upload
        api_response = api_instance.create_pdf_template(template_document, template_name, wait=wait, template_description=template_description, template_parent_folder_id=template_parent_folder_id)
        print("The response of PDFApi->create_pdf_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_pdf_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_document** | **bytearray**|  | 
 **template_name** | **str**|  | 
 **wait** | **bool**| Wait for template document to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) | [optional] [default to True]
 **template_description** | **str**|  | [optional] 
 **template_parent_folder_id** | **str**|  | [optional] 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns a pending template |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pdf_template_from_upload**
> TemplatePreview create_pdf_template_from_upload(data)

Create a new PDF template from a cached presign upload

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_pdf_template import CreatePdfTemplate
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data = docspring.CreatePdfTemplate() # CreatePdfTemplate | 

    try:
        # Create a new PDF template from a cached presign upload
        api_response = api_instance.create_pdf_template_from_upload(data)
        print("The response of PDFApi->create_pdf_template_from_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->create_pdf_template_from_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreatePdfTemplate**](CreatePdfTemplate.md)|  | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns a pending template |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> Folder delete_folder(folder_id)

Delete a folder

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    folder_id = 'fld_1234567890abcdef01' # str | 

    try:
        # Delete a folder
        api_response = api_instance.delete_folder(folder_id)
        print("The response of PDFApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | folder doesn&#39;t exist |  -  |
**422** | folder has contents |  -  |
**200** | folder is empty |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> TemplateDeleteResponse delete_template(template_id, version=version)

Delete a template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_delete_response import TemplateDeleteResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    version = '0.1.0' # str |  (optional)

    try:
        # Delete a template
        api_response = api_instance.delete_template(template_id, version=version)
        print("The response of PDFApi->delete_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

[**TemplateDeleteResponse**](TemplateDeleteResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template version deleted successfully |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_combined_submission**
> CombinedSubmission expire_combined_submission(combined_submission_id)

Expire a combined submission

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_submission import CombinedSubmission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    combined_submission_id = 'com_1234567890abcdef01' # str | 

    try:
        # Expire a combined submission
        api_response = api_instance.expire_combined_submission(combined_submission_id)
        print("The response of PDFApi->expire_combined_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->expire_combined_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_submission_id** | **str**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | submission was expired |  -  |
**404** | combined submission not found |  -  |
**403** | test API token used |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_submission**
> SubmissionPreview expire_submission(submission_id)

Expire a PDF submission

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_preview import SubmissionPreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | 

    try:
        # Expire a PDF submission
        api_response = api_instance.expire_submission(submission_id)
        print("The response of PDFApi->expire_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->expire_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 

### Return type

[**SubmissionPreview**](SubmissionPreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | submission was expired |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |
**403** | test API token used |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pdf**
> CreateSubmissionResponse generate_pdf(template_id, submission, wait=wait)

Generates a new PDF

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_pdf_submission_data import CreatePdfSubmissionData
from docspring.models.create_submission_response import CreateSubmissionResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    submission = docspring.CreatePdfSubmissionData() # CreatePdfSubmissionData | 
    wait = True # bool | Wait for submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) (optional) (default to True)

    try:
        # Generates a new PDF
        api_response = api_instance.generate_pdf(template_id, submission, wait=wait)
        print("The response of PDFApi->generate_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->generate_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **submission** | [**CreatePdfSubmissionData**](CreatePdfSubmissionData.md)|  | 
 **wait** | **bool**| Wait for submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) | [optional] [default to True]

### Return type

[**CreateSubmissionResponse**](CreateSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | submission created |  -  |
**422** | invalid request |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pdf_for_html_template**
> CreateSubmissionResponse generate_pdf_for_html_template(template_id, submission, wait=wait)

Generates a new PDF for an HTML template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_html_submission_data import CreateHtmlSubmissionData
from docspring.models.create_submission_response import CreateSubmissionResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_HTML567890abcdef01' # str | 
    submission = docspring.CreateHtmlSubmissionData() # CreateHtmlSubmissionData | 
    wait = True # bool | Wait for submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) (optional) (default to True)

    try:
        # Generates a new PDF for an HTML template
        api_response = api_instance.generate_pdf_for_html_template(template_id, submission, wait=wait)
        print("The response of PDFApi->generate_pdf_for_html_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->generate_pdf_for_html_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **submission** | [**CreateHtmlSubmissionData**](CreateHtmlSubmissionData.md)|  | 
 **wait** | **bool**| Wait for submission to be processed before returning. Set to false to return immediately. Default: true (on sync.* subdomain) | [optional] [default to True]

### Return type

[**CreateSubmissionResponse**](CreateSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | submission created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_preview**
> SuccessErrorResponse generate_preview(submission_id)

Generated a preview PDF for partially completed data requests

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.success_error_response import SuccessErrorResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | 

    try:
        # Generated a preview PDF for partially completed data requests
        api_response = api_instance.generate_preview(submission_id)
        print("The response of PDFApi->generate_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->generate_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 

### Return type

[**SuccessErrorResponse**](SuccessErrorResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | preview was successfully requested |  -  |
**404** | submission not found |  -  |
**422** | error requesting preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_combined_submission**
> CombinedSubmission get_combined_submission(combined_submission_id)

Check the status of a combined submission (merged PDFs)

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_submission import CombinedSubmission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    combined_submission_id = 'com_1234567890abcdef01' # str | 

    try:
        # Check the status of a combined submission (merged PDFs)
        api_response = api_instance.get_combined_submission(combined_submission_id)
        print("The response of PDFApi->get_combined_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_combined_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_submission_id** | **str**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | processed combined submission found |  -  |
**404** | combined submission not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_request**
> SubmissionDataRequestShow get_data_request(data_request_id)

Look up a submission data request

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_data_request_show import SubmissionDataRequestShow
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data_request_id = 'drq_1234567890abcdef01' # str | 

    try:
        # Look up a submission data request
        api_response = api_instance.get_data_request(data_request_id)
        print("The response of PDFApi->get_data_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_data_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 

### Return type

[**SubmissionDataRequestShow**](SubmissionDataRequestShow.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | completed submission data request found |  -  |
**404** | submission data request not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_template**
> Template get_full_template(template_id)

Fetch the full attributes for a PDF template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template import Template
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 

    try:
        # Fetch the full attributes for a PDF template
        api_response = api_instance.get_full_template(template_id)
        print("The response of PDFApi->get_full_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_full_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template found |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presign_url**
> UploadPresignResponse get_presign_url()

Get a presigned URL so that you can upload a file to our AWS S3 bucket

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.upload_presign_response import UploadPresignResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)

    try:
        # Get a presigned URL so that you can upload a file to our AWS S3 bucket
        api_response = api_instance.get_presign_url()
        print("The response of PDFApi->get_presign_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_presign_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UploadPresignResponse**](UploadPresignResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | presign URL generated |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> Submission get_submission(submission_id, include_data=include_data)

Check the status of a PDF

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission import Submission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    submission_id = 'sub_1234567890abcdef01' # str | 
    include_data = true # bool |  (optional)

    try:
        # Check the status of a PDF
        api_response = api_instance.get_submission(submission_id, include_data=include_data)
        print("The response of PDFApi->get_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 
 **include_data** | **bool**|  | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | processed submission found |  -  |
**404** | submission not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_batch**
> SubmissionBatchWithSubmissions get_submission_batch(submission_batch_id, include_submissions=include_submissions)

Check the status of a submission batch job

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.submission_batch_with_submissions import SubmissionBatchWithSubmissions
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    submission_batch_id = 'sbb_1234567890abcdef01' # str | 
    include_submissions = true # bool |  (optional)

    try:
        # Check the status of a submission batch job
        api_response = api_instance.get_submission_batch(submission_batch_id, include_submissions=include_submissions)
        print("The response of PDFApi->get_submission_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_submission_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_batch_id** | **str**|  | 
 **include_submissions** | **bool**|  | [optional] 

### Return type

[**SubmissionBatchWithSubmissions**](SubmissionBatchWithSubmissions.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | processed submission batch found |  -  |
**404** | submission batch not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplatePreview get_template(template_id)

Check the status of an uploaded template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 

    try:
        # Check the status of an uploaded template
        api_response = api_instance.get_template(template_id)
        print("The response of PDFApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template found |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_schema**
> JsonSchema get_template_schema(template_id)

Fetch the JSON schema for a template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.json_schema import JsonSchema
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 

    try:
        # Fetch the JSON schema for a template
        api_response = api_instance.get_template_schema(template_id)
        print("The response of PDFApi->get_template_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->get_template_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**JsonSchema**](JsonSchema.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template found |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_combined_submissions**
> List[CombinedSubmission] list_combined_submissions(page=page, per_page=per_page)

Get a list of all combined submissions

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.combined_submission import CombinedSubmission
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    page = 2 # int | Default: 1 (optional)
    per_page = 1 # int | Default: 50 (optional)

    try:
        # Get a list of all combined submissions
        api_response = api_instance.list_combined_submissions(page=page, per_page=per_page)
        print("The response of PDFApi->list_combined_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->list_combined_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Default: 1 | [optional] 
 **per_page** | **int**| Default: 50 | [optional] 

### Return type

[**List[CombinedSubmission]**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | enumerate all combined submissions |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> List[Folder] list_folders(parent_folder_id=parent_folder_id)

Get a list of all folders

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    parent_folder_id = 'fld_1234567890abcdef02' # str | Filter By Folder Id (optional)

    try:
        # Get a list of all folders
        api_response = api_instance.list_folders(parent_folder_id=parent_folder_id)
        print("The response of PDFApi->list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->list_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_folder_id** | **str**| Filter By Folder Id | [optional] 

### Return type

[**List[Folder]**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | enumerate all folders |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_submissions**
> ListSubmissionsResponse list_submissions(cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)

List all submissions

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.list_submissions_response import ListSubmissionsResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    cursor = 'sub_1234567890abcdef12' # str |  (optional)
    limit = 3 # float |  (optional)
    created_after = '2019-01-01T09:00:00-05:00' # str |  (optional)
    created_before = '2020-01-01T09:00:00.000+0200' # str |  (optional)
    type = 'test' # str |  (optional)
    include_data = true # bool |  (optional)

    try:
        # List all submissions
        api_response = api_instance.list_submissions(cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)
        print("The response of PDFApi->list_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->list_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **created_after** | **str**|  | [optional] 
 **created_before** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_data** | **bool**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listing submissions |  -  |
**422** | invalid type |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_submissions**
> ListSubmissionsResponse list_template_submissions(template_id, cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)

List all submissions for a given template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.list_submissions_response import ListSubmissionsResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef02' # str | 
    cursor = 'cursor_example' # str |  (optional)
    limit = 3.4 # float |  (optional)
    created_after = 'created_after_example' # str |  (optional)
    created_before = 'created_before_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    include_data = true # bool |  (optional)

    try:
        # List all submissions for a given template
        api_response = api_instance.list_template_submissions(template_id, cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)
        print("The response of PDFApi->list_template_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->list_template_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **created_after** | **str**|  | [optional] 
 **created_before** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_data** | **bool**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listing submissions |  -  |
**404** | invalid template id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> List[TemplatePreview] list_templates(query=query, parent_folder_id=parent_folder_id, page=page, per_page=per_page)

Get a list of all templates

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    query = '2' # str | Search By Name (optional)
    parent_folder_id = 'fld_1234567890abcdef01' # str | Filter By Folder Id (optional)
    page = 2 # int | Default: 1 (optional)
    per_page = 1 # int | Default: 50 (optional)

    try:
        # Get a list of all templates
        api_response = api_instance.list_templates(query=query, parent_folder_id=parent_folder_id, page=page, per_page=per_page)
        print("The response of PDFApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search By Name | [optional] 
 **parent_folder_id** | **str**| Filter By Folder Id | [optional] 
 **page** | **int**| Default: 1 | [optional] 
 **per_page** | **int**| Default: 50 | [optional] 

### Return type

[**List[TemplatePreview]**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | enumerate all templates |  -  |
**404** | filter templates by invalid folder id |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_to_folder**
> Folder move_folder_to_folder(folder_id, data)

Move a folder

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.models.move_folder_data import MoveFolderData
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    folder_id = 'fld_1234567890abcdef01' # str | 
    data = docspring.MoveFolderData() # MoveFolderData | 

    try:
        # Move a folder
        api_response = api_instance.move_folder_to_folder(folder_id, data)
        print("The response of PDFApi->move_folder_to_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->move_folder_to_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **data** | [**MoveFolderData**](MoveFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | parent folder doesn&#39;t exist |  -  |
**200** | move to root folder |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_template_to_folder**
> TemplatePreview move_template_to_folder(template_id, data)

Move Template to folder

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.move_template_data import MoveTemplateData
from docspring.models.template_preview import TemplatePreview
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    data = docspring.MoveTemplateData() # MoveTemplateData | 

    try:
        # Move Template to folder
        api_response = api_instance.move_template_to_folder(template_id, data)
        print("The response of PDFApi->move_template_to_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->move_template_to_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **data** | [**MoveTemplateData**](MoveTemplateData.md)|  | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | move template success |  -  |
**404** | folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_template_version**
> TemplatePublishVersionResponse publish_template_version(template_id, data)

Publish a template version

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.publish_version_data import PublishVersionData
from docspring.models.template_publish_version_response import TemplatePublishVersionResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    data = docspring.PublishVersionData() # PublishVersionData | 

    try:
        # Publish a template version
        api_response = api_instance.publish_template_version(template_id, data)
        print("The response of PDFApi->publish_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->publish_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **data** | [**PublishVersionData**](PublishVersionData.md)|  | 

### Return type

[**TemplatePublishVersionResponse**](TemplatePublishVersionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | version published successfully |  -  |
**422** | invalid version type |  -  |
**404** | template not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> Folder rename_folder(folder_id, data)

Rename a folder

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.folder import Folder
from docspring.models.rename_folder_data import RenameFolderData
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    folder_id = 'fld_1234567890abcdef01' # str | 
    data = docspring.RenameFolderData() # RenameFolderData | 

    try:
        # Rename a folder
        api_response = api_instance.rename_folder(folder_id, data)
        print("The response of PDFApi->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->rename_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **data** | [**RenameFolderData**](RenameFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | name already exist |  -  |
**404** | folder doesn&#39;t belong to me |  -  |
**200** | successful rename |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_template_version**
> SuccessErrorResponse restore_template_version(template_id, data)

Restore a template version

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.restore_version_data import RestoreVersionData
from docspring.models.success_error_response import SuccessErrorResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef01' # str | 
    data = docspring.RestoreVersionData() # RestoreVersionData | 

    try:
        # Restore a template version
        api_response = api_instance.restore_template_version(template_id, data)
        print("The response of PDFApi->restore_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->restore_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **data** | [**RestoreVersionData**](RestoreVersionData.md)|  | 

### Return type

[**SuccessErrorResponse**](SuccessErrorResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | version restored successfully |  -  |
**422** | draft version not allowed |  -  |
**404** | template version not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_authentication**
> SuccessErrorResponse test_authentication()

Test Authentication

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.success_error_response import SuccessErrorResponse
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)

    try:
        # Test Authentication
        api_response = api_instance.test_authentication()
        print("The response of PDFApi->test_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->test_authentication: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessErrorResponse**](SuccessErrorResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | authentication succeeded |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_request**
> CreateSubmissionDataRequestResponse update_data_request(data_request_id, data)

Update a submission data request

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.create_submission_data_request_response import CreateSubmissionDataRequestResponse
from docspring.models.update_submission_data_request_data import UpdateSubmissionDataRequestData
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    data_request_id = 'drq_1234567890abcdef01' # str | 
    data = docspring.UpdateSubmissionDataRequestData() # UpdateSubmissionDataRequestData | 

    try:
        # Update a submission data request
        api_response = api_instance.update_data_request(data_request_id, data)
        print("The response of PDFApi->update_data_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->update_data_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 
 **data** | [**UpdateSubmissionDataRequestData**](UpdateSubmissionDataRequestData.md)|  | 

### Return type

[**CreateSubmissionDataRequestResponse**](CreateSubmissionDataRequestResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | submission data request updated |  -  |
**422** | invalid request |  -  |
**404** | submission data request not found |  -  |
**401** | authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> SuccessMultipleErrorsResponse update_template(template_id, data)

Update a Template

### Example

* Basic Authentication (api_token_basic):

```python
import docspring
from docspring.models.success_multiple_errors_response import SuccessMultipleErrorsResponse
from docspring.models.update_html_template import UpdateHtmlTemplate
from docspring.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sync.api.docspring.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = docspring.Configuration(
    host = "https://sync.api.docspring.com/api/v1"
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
    api_instance = docspring.PDFApi(api_client)
    template_id = 'tpl_1234567890abcdef03' # str | 
    data = docspring.UpdateHtmlTemplate() # UpdateHtmlTemplate | 

    try:
        # Update a Template
        api_response = api_instance.update_template(template_id, data)
        print("The response of PDFApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **data** | [**UpdateHtmlTemplate**](UpdateHtmlTemplate.md)|  | 

### Return type

[**SuccessMultipleErrorsResponse**](SuccessMultipleErrorsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | update template success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

