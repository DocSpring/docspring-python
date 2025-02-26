# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.submission_preview import SubmissionPreview

class TestSubmissionPreview(unittest.TestCase):
    """SubmissionPreview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubmissionPreview:
        """Test SubmissionPreview
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubmissionPreview`
        """
        model = SubmissionPreview()
        if include_optional:
            return SubmissionPreview(
                batch_id = '',
                data_requests = [
                    docspring.models.submission_data_request.submission_data_request(
                        id = '', 
                        email = '', 
                        name = '', 
                        order = 56, 
                        sort_order = 56, 
                        fields = [
                            ''
                            ], 
                        metadata = docspring.models.metadata.metadata(), 
                        state = 'pending', 
                        viewed_at = '', 
                        completed_at = '', 
                        data = docspring.models.data.data(), 
                        auth_type = 'none', 
                        auth_second_factor_type = 'none', 
                        auth_provider = '', 
                        auth_session_started_at = '', 
                        auth_session_id_hash = '', 
                        auth_user_id_hash = '', 
                        auth_username_hash = '', 
                        auth_phone_number_hash = '', 
                        ip_address = '', 
                        user_agent = '', )
                    ],
                editable = True,
                expired = True,
                expires_at = '',
                id = '',
                json_schema_errors = [
                    ''
                    ],
                metadata = docspring.models.metadata.metadata(),
                password = '',
                processed_at = '',
                state = 'pending',
                template_id = '',
                test = True,
                truncated_text = docspring.models.truncated_text.truncated_text(),
                pdf_hash = '',
                download_url = '',
                permanent_download_url = '',
                preview_download_url = '',
                preview_generated_at = '',
                audit_trail_download_url = '',
                actions = [
                    docspring.models.submission_action.submission_action(
                        id = '', 
                        integration_id = '', 
                        state = 'pending', 
                        action_type = 'webhook', 
                        action_category = 'notification', 
                        result_data = docspring.models.result_data.result_data(), )
                    ]
            )
        else:
            return SubmissionPreview(
                batch_id = '',
                data_requests = [
                    docspring.models.submission_data_request.submission_data_request(
                        id = '', 
                        email = '', 
                        name = '', 
                        order = 56, 
                        sort_order = 56, 
                        fields = [
                            ''
                            ], 
                        metadata = docspring.models.metadata.metadata(), 
                        state = 'pending', 
                        viewed_at = '', 
                        completed_at = '', 
                        data = docspring.models.data.data(), 
                        auth_type = 'none', 
                        auth_second_factor_type = 'none', 
                        auth_provider = '', 
                        auth_session_started_at = '', 
                        auth_session_id_hash = '', 
                        auth_user_id_hash = '', 
                        auth_username_hash = '', 
                        auth_phone_number_hash = '', 
                        ip_address = '', 
                        user_agent = '', )
                    ],
                editable = True,
                expired = True,
                expires_at = '',
                id = '',
                json_schema_errors = [
                    ''
                    ],
                metadata = docspring.models.metadata.metadata(),
                password = '',
                processed_at = '',
                state = 'pending',
                template_id = '',
                test = True,
                truncated_text = docspring.models.truncated_text.truncated_text(),
                pdf_hash = '',
                download_url = '',
                permanent_download_url = '',
                preview_download_url = '',
                preview_generated_at = '',
                audit_trail_download_url = '',
                actions = [
                    docspring.models.submission_action.submission_action(
                        id = '', 
                        integration_id = '', 
                        state = 'pending', 
                        action_type = 'webhook', 
                        action_category = 'notification', 
                        result_data = docspring.models.result_data.result_data(), )
                    ],
        )
        """

    def testSubmissionPreview(self):
        """Test SubmissionPreview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
