# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.create_submission_data_request_event_response import CreateSubmissionDataRequestEventResponse

class TestCreateSubmissionDataRequestEventResponse(unittest.TestCase):
    """CreateSubmissionDataRequestEventResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubmissionDataRequestEventResponse:
        """Test CreateSubmissionDataRequestEventResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubmissionDataRequestEventResponse`
        """
        model = CreateSubmissionDataRequestEventResponse()
        if include_optional:
            return CreateSubmissionDataRequestEventResponse(
                status = 'success',
                event = docspring.models.submission_data_request_event.submission_data_request_event(
                    id = '', 
                    submission_id = '', 
                    submission_data_request_id = '', 
                    event_type = 'send_request', 
                    message_type = 'email', 
                    message_recipient = '', 
                    occurred_at = '', ),
                errors = [
                    ''
                    ]
            )
        else:
            return CreateSubmissionDataRequestEventResponse(
                status = 'success',
                event = docspring.models.submission_data_request_event.submission_data_request_event(
                    id = '', 
                    submission_id = '', 
                    submission_data_request_id = '', 
                    event_type = 'send_request', 
                    message_type = 'email', 
                    message_recipient = '', 
                    occurred_at = '', ),
        )
        """

    def testCreateSubmissionDataRequestEventResponse(self):
        """Test CreateSubmissionDataRequestEventResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
