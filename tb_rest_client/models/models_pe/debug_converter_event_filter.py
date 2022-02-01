# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from .event_filter import EventFilter


class DebugConverterEventFilter(EventFilter):
    """
    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'bool',
        '_in': 'str',
        'metadata': 'str',
        'out': 'str',
        'type': 'str',
        'event_type': 'str',
        'server': 'str',
        'error_str': 'str'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'error': 'error',
        '_in': 'in',
        'metadata': 'metadata',
        'out': 'out',
        'type': 'type',
        'event_type': 'eventType',
        'server': 'server',
        'error_str': 'errorStr'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, error=None, _in=None, metadata=None, out=None, type=None, event_type=None, server=None, error_str=None, *args, **kwargs):  # noqa: E501
        """DebugConverterEventFilter - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self.__in = None
        self._metadata = None
        self._out = None
        self._type = None
        self._event_type = None
        self._server = None
        self._error_str = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if _in is not None:
            self._in = _in
        if metadata is not None:
            self.metadata = metadata
        if out is not None:
            self.out = out
        if type is not None:
            self.type = type
        self.event_type = event_type
        if server is not None:
            self.server = server
        if error_str is not None:
            self.error_str = error_str
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def error(self):
        """Gets the error of this DebugConverterEventFilter.  # noqa: E501


        :return: The error of this DebugConverterEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DebugConverterEventFilter.


        :param error: The error of this DebugConverterEventFilter.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def _in(self):
        """Gets the _in of this DebugConverterEventFilter.  # noqa: E501


        :return: The _in of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this DebugConverterEventFilter.


        :param _in: The _in of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self.__in = _in

    @property
    def metadata(self):
        """Gets the metadata of this DebugConverterEventFilter.  # noqa: E501


        :return: The metadata of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DebugConverterEventFilter.


        :param metadata: The metadata of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def out(self):
        """Gets the out of this DebugConverterEventFilter.  # noqa: E501


        :return: The out of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this DebugConverterEventFilter.


        :param out: The out of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._out = out

    @property
    def type(self):
        """Gets the type of this DebugConverterEventFilter.  # noqa: E501


        :return: The type of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DebugConverterEventFilter.


        :param type: The type of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def event_type(self):
        """Gets the event_type of this DebugConverterEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this DebugConverterEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_CONVERTER", "DEBUG_INTEGRATION", "DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def server(self):
        """Gets the server of this DebugConverterEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this DebugConverterEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def error_str(self):
        """Gets the error_str of this DebugConverterEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this DebugConverterEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DebugConverterEventFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DebugConverterEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
