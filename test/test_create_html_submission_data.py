# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.create_html_submission_data import CreateHtmlSubmissionData

class TestCreateHtmlSubmissionData(unittest.TestCase):
    """CreateHtmlSubmissionData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateHtmlSubmissionData:
        """Test CreateHtmlSubmissionData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateHtmlSubmissionData`
        """
        model = CreateHtmlSubmissionData()
        if include_optional:
            return CreateHtmlSubmissionData(
                css = '',
                data = docspring.models.submission_data.submission_data(),
                editable = True,
                expires_in = 56,
                field_overrides = docspring.models.submission_field_overrides.submission_field_overrides(),
                html = '',
                metadata = docspring.models.submission_metadata.submission_metadata(),
                password = '',
                test = True,
                version = ''
            )
        else:
            return CreateHtmlSubmissionData(
        )
        """

    def testCreateHtmlSubmissionData(self):
        """Test CreateHtmlSubmissionData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
