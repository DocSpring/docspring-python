# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_data_request_submission_id_footers** | **bool** |  | 
**allow_additional_properties** | **bool** |  | 
**description** | **str** |  | 
**document_filename** | **str** |  | 
**document_md5** | **str** |  | 
**document_parse_error** | **bool** |  | 
**document_processed** | **bool** |  | 
**document_state** | **str** |  | 
**document_url** | **str** |  | 
**editable_submissions** | **bool** |  | 
**embed_domains** | **str** |  | 
**encrypt_pdfs_password** | **str** |  | 
**encrypt_pdfs** | **bool** |  | 
**expiration_interval** | **str** |  | 
**expire_after** | **int** |  | 
**expire_submissions** | **bool** |  | 
**external_predefined_fields_template_id** | **str** |  | 
**external_predefined_fields_template_name** | **str** |  | 
**first_template** | **bool** |  | 
**id** | **str** |  | 
**locked** | **bool** |  | 
**merge_audit_trail_pdf** | **bool** |  | 
**name** | **str** |  | 
**page_count** | **int** |  | 
**page_dimensions** | **List[List[float]]** |  | 
**parent_folder_id** | **str** |  | 
**path** | **str** |  | 
**permanent_document_url** | **str** |  | 
**public_submissions** | **bool** |  | 
**public_web_form** | **bool** |  | 
**redirect_url** | **str** |  | 
**slack_webhook_url** | **str** |  | 
**template_type** | **str** |  | 
**updated_at** | **str** |  | 
**webhook_url** | **str** |  | 
**demo** | **bool** |  | 
**defaults** | **object** |  | 
**field_order** | **List[List[float]]** |  | 
**fields** | **object** |  | 
**footer_html** | **str** |  | 
**header_html** | **str** |  | 
**html_engine_options** | **object** |  | 
**html** | **str** |  | 
**predefined_fields** | **List[object]** |  | 
**scss** | **str** |  | 
**shared_field_data** | **object** |  | 

## Example

```python
from docspring.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


