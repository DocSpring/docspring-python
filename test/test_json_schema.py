# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from docspring.models.json_schema import JsonSchema

class TestJsonSchema(unittest.TestCase):
    """JsonSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonSchema:
        """Test JsonSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonSchema`
        """
        model = JsonSchema()
        if include_optional:
            return JsonSchema(
                var_schema = '',
                id = '',
                title = '',
                description = '',
                definitions = None,
                type = '',
                properties = None,
                additional_properties = True,
                required = [
                    ''
                    ]
            )
        else:
            return JsonSchema(
        )
        """

    def testJsonSchema(self):
        """Test JsonSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
