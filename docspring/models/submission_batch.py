# coding: utf-8

"""
    API v1

    DocSpring is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SubmissionBatch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pending_count': 'int',
        'completion_percentage': 'int',
        'metadata': 'object',
        'total_count': 'int',
        'submissions': 'list[Submission]',
        'processed_at': 'str',
        'id': 'str',
        'state': 'str',
        'error_count': 'int'
    }

    attribute_map = {
        'pending_count': 'pending_count',
        'completion_percentage': 'completion_percentage',
        'metadata': 'metadata',
        'total_count': 'total_count',
        'submissions': 'submissions',
        'processed_at': 'processed_at',
        'id': 'id',
        'state': 'state',
        'error_count': 'error_count'
    }

    def __init__(self, pending_count=None, completion_percentage=None, metadata=None, total_count=None, submissions=None, processed_at=None, id=None, state=None, error_count=None):  # noqa: E501
        """SubmissionBatch - a model defined in OpenAPI"""  # noqa: E501

        self._pending_count = None
        self._completion_percentage = None
        self._metadata = None
        self._total_count = None
        self._submissions = None
        self._processed_at = None
        self._id = None
        self._state = None
        self._error_count = None
        self.discriminator = None

        if pending_count is not None:
            self.pending_count = pending_count
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if metadata is not None:
            self.metadata = metadata
        if total_count is not None:
            self.total_count = total_count
        if submissions is not None:
            self.submissions = submissions
        self.processed_at = processed_at
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if error_count is not None:
            self.error_count = error_count

    @property
    def pending_count(self):
        """Gets the pending_count of this SubmissionBatch.  # noqa: E501


        :return: The pending_count of this SubmissionBatch.  # noqa: E501
        :rtype: int
        """
        return self._pending_count

    @pending_count.setter
    def pending_count(self, pending_count):
        """Sets the pending_count of this SubmissionBatch.


        :param pending_count: The pending_count of this SubmissionBatch.  # noqa: E501
        :type: int
        """

        self._pending_count = pending_count

    @property
    def completion_percentage(self):
        """Gets the completion_percentage of this SubmissionBatch.  # noqa: E501


        :return: The completion_percentage of this SubmissionBatch.  # noqa: E501
        :rtype: int
        """
        return self._completion_percentage

    @completion_percentage.setter
    def completion_percentage(self, completion_percentage):
        """Sets the completion_percentage of this SubmissionBatch.


        :param completion_percentage: The completion_percentage of this SubmissionBatch.  # noqa: E501
        :type: int
        """

        self._completion_percentage = completion_percentage

    @property
    def metadata(self):
        """Gets the metadata of this SubmissionBatch.  # noqa: E501


        :return: The metadata of this SubmissionBatch.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SubmissionBatch.


        :param metadata: The metadata of this SubmissionBatch.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def total_count(self):
        """Gets the total_count of this SubmissionBatch.  # noqa: E501


        :return: The total_count of this SubmissionBatch.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SubmissionBatch.


        :param total_count: The total_count of this SubmissionBatch.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def submissions(self):
        """Gets the submissions of this SubmissionBatch.  # noqa: E501


        :return: The submissions of this SubmissionBatch.  # noqa: E501
        :rtype: list[Submission]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this SubmissionBatch.


        :param submissions: The submissions of this SubmissionBatch.  # noqa: E501
        :type: list[Submission]
        """

        self._submissions = submissions

    @property
    def processed_at(self):
        """Gets the processed_at of this SubmissionBatch.  # noqa: E501


        :return: The processed_at of this SubmissionBatch.  # noqa: E501
        :rtype: str
        """
        return self._processed_at

    @processed_at.setter
    def processed_at(self, processed_at):
        """Sets the processed_at of this SubmissionBatch.


        :param processed_at: The processed_at of this SubmissionBatch.  # noqa: E501
        :type: str
        """

        self._processed_at = processed_at

    @property
    def id(self):
        """Gets the id of this SubmissionBatch.  # noqa: E501


        :return: The id of this SubmissionBatch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmissionBatch.


        :param id: The id of this SubmissionBatch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this SubmissionBatch.  # noqa: E501


        :return: The state of this SubmissionBatch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubmissionBatch.


        :param state: The state of this SubmissionBatch.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "processed", "error"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def error_count(self):
        """Gets the error_count of this SubmissionBatch.  # noqa: E501


        :return: The error_count of this SubmissionBatch.  # noqa: E501
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this SubmissionBatch.


        :param error_count: The error_count of this SubmissionBatch.  # noqa: E501
        :type: int
        """

        self._error_count = error_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubmissionBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
