# coding: utf-8

"""
    API v1

    DocSpring is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "docspring"
VERSION = "1.3.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="API v1",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "API v1"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    DocSpring is a service that helps you fill out and sign PDF templates.  # noqa: E501
    """
)
