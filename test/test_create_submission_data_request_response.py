# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.create_submission_data_request_response import CreateSubmissionDataRequestResponse

class TestCreateSubmissionDataRequestResponse(unittest.TestCase):
    """CreateSubmissionDataRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubmissionDataRequestResponse:
        """Test CreateSubmissionDataRequestResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubmissionDataRequestResponse`
        """
        model = CreateSubmissionDataRequestResponse()
        if include_optional:
            return CreateSubmissionDataRequestResponse(
                status = 'success',
                data_request = docspring.models.submission_data_request_show.submission_data_request_show(
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
                    user_agent = '', 
                    submission_id = '', ),
                errors = [
                    ''
                    ]
            )
        else:
            return CreateSubmissionDataRequestResponse(
                status = 'success',
                data_request = docspring.models.submission_data_request_show.submission_data_request_show(
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
                    user_agent = '', 
                    submission_id = '', ),
        )
        """

    def testCreateSubmissionDataRequestResponse(self):
        """Test CreateSubmissionDataRequestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
