# coding: utf-8

"""
    Hotelspro Api Client

    Hotelspro Api Client

    OpenAPI spec version: 2.0.0
    Contact: clientintegration@hotelspro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Results(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hotel_code': 'str',
        'checkout': 'str',
        'checkin': 'str',
        'destination_code': 'str',
        'products': 'list[Product]'
    }

    attribute_map = {
        'hotel_code': 'hotel_code',
        'checkout': 'checkout',
        'checkin': 'checkin',
        'destination_code': 'destination_code',
        'products': 'products'
    }

    def __init__(self, hotel_code=None, checkout=None, checkin=None, destination_code=None, products=None):
        """
        Results - a model defined in Swagger
        """

        self._hotel_code = None
        self._checkout = None
        self._checkin = None
        self._destination_code = None
        self._products = None

        if hotel_code is not None:
          self.hotel_code = hotel_code
        if checkout is not None:
          self.checkout = checkout
        if checkin is not None:
          self.checkin = checkin
        if destination_code is not None:
          self.destination_code = destination_code
        if products is not None:
          self.products = products

    @property
    def hotel_code(self):
        """
        Gets the hotel_code of this Results.

        :return: The hotel_code of this Results.
        :rtype: str
        """
        return self._hotel_code

    @hotel_code.setter
    def hotel_code(self, hotel_code):
        """
        Sets the hotel_code of this Results.

        :param hotel_code: The hotel_code of this Results.
        :type: str
        """

        self._hotel_code = hotel_code

    @property
    def checkout(self):
        """
        Gets the checkout of this Results.

        :return: The checkout of this Results.
        :rtype: str
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """
        Sets the checkout of this Results.

        :param checkout: The checkout of this Results.
        :type: str
        """

        self._checkout = checkout

    @property
    def checkin(self):
        """
        Gets the checkin of this Results.

        :return: The checkin of this Results.
        :rtype: str
        """
        return self._checkin

    @checkin.setter
    def checkin(self, checkin):
        """
        Sets the checkin of this Results.

        :param checkin: The checkin of this Results.
        :type: str
        """

        self._checkin = checkin

    @property
    def destination_code(self):
        """
        Gets the destination_code of this Results.

        :return: The destination_code of this Results.
        :rtype: str
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """
        Sets the destination_code of this Results.

        :param destination_code: The destination_code of this Results.
        :type: str
        """

        self._destination_code = destination_code

    @property
    def products(self):
        """
        Gets the products of this Results.

        :return: The products of this Results.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this Results.

        :param products: The products of this Results.
        :type: list[Product]
        """

        self._products = products

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other