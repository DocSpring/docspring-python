# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.folder import Folder

class TestFolder(unittest.TestCase):
    """Folder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Folder:
        """Test Folder
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Folder`
        """
        model = Folder()
        if include_optional:
            return Folder(
                id = '',
                name = '',
                path = '',
                parent_folder_id = ''
            )
        else:
            return Folder(
                id = '',
                name = '',
                path = '',
                parent_folder_id = '',
        )
        """

    def testFolder(self):
        """Test Folder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
