# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connection import Connection  # noqa: F401,E501
from tapi_server.models.connectivity_service import ConnectivityService  # noqa: F401,E501
from tapi_server import util


class ConnectivityContext(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, connectivity_service: List[ConnectivityService]=None, connection: List[Connection]=None):  # noqa: E501
        """ConnectivityContext - a model defined in Swagger

        :param connectivity_service: The connectivity_service of this ConnectivityContext.  # noqa: E501
        :type connectivity_service: List[ConnectivityService]
        :param connection: The connection of this ConnectivityContext.  # noqa: E501
        :type connection: List[Connection]
        """
        self.swagger_types = {
            'connectivity_service': List[ConnectivityService],
            'connection': List[Connection]
        }

        self.attribute_map = {
            'connectivity_service': 'connectivity-service',
            'connection': 'connection'
        }

        self._connectivity_service = connectivity_service
        self._connection = connection

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectivityContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The connectivity-context of this ConnectivityContext.  # noqa: E501
        :rtype: ConnectivityContext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def connectivity_service(self) -> List[ConnectivityService]:
        """Gets the connectivity_service of this ConnectivityContext.


        :return: The connectivity_service of this ConnectivityContext.
        :rtype: List[ConnectivityService]
        """
        return self._connectivity_service

    @connectivity_service.setter
    def connectivity_service(self, connectivity_service: List[ConnectivityService]):
        """Sets the connectivity_service of this ConnectivityContext.


        :param connectivity_service: The connectivity_service of this ConnectivityContext.
        :type connectivity_service: List[ConnectivityService]
        """

        self._connectivity_service = connectivity_service

    @property
    def connection(self) -> List[Connection]:
        """Gets the connection of this ConnectivityContext.


        :return: The connection of this ConnectivityContext.
        :rtype: List[Connection]
        """
        return self._connection

    @connection.setter
    def connection(self, connection: List[Connection]):
        """Sets the connection of this ConnectivityContext.


        :param connection: The connection of this ConnectivityContext.
        :type connection: List[Connection]
        """

        self._connection = connection