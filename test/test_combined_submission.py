# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.combined_submission import CombinedSubmission

class TestCombinedSubmission(unittest.TestCase):
    """CombinedSubmission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CombinedSubmission:
        """Test CombinedSubmission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CombinedSubmission`
        """
        model = CombinedSubmission()
        if include_optional:
            return CombinedSubmission(
                id = '',
                state = 'pending',
                expired = True,
                expires_in = 56,
                expires_at = '',
                processed_at = '',
                error_message = '',
                submission_ids = [
                    ''
                    ],
                source_pdfs = [
                    None
                    ],
                metadata = None,
                password = '',
                pdf_hash = '',
                download_url = '',
                actions = [
                    docspring.models.combined_submission_action.combined_submission_action(
                        id = '', 
                        integration_id = '', 
                        state = 'pending', 
                        action_type = 'webhook', 
                        action_category = 'notification', 
                        result_data = docspring.models.result_data.result_data(), )
                    ]
            )
        else:
            return CombinedSubmission(
                id = '',
                state = 'pending',
                expired = True,
                expires_in = 56,
                expires_at = '',
                processed_at = '',
                error_message = '',
                submission_ids = [
                    ''
                    ],
                source_pdfs = [
                    None
                    ],
                metadata = None,
                password = '',
                pdf_hash = '',
                download_url = '',
                actions = [
                    docspring.models.combined_submission_action.combined_submission_action(
                        id = '', 
                        integration_id = '', 
                        state = 'pending', 
                        action_type = 'webhook', 
                        action_category = 'notification', 
                        result_data = docspring.models.result_data.result_data(), )
                    ],
        )
        """

    def testCombinedSubmission(self):
        """Test CombinedSubmission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
