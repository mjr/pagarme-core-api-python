# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.get_customer_response

class GetAccessTokenResponse(object):

    """Implementation of the 'GetAccessTokenResponse' model.

    Response object for getting a access token

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "code":'code',
        "status":'status',
        "created_at":'created_at',
        "customer":'customer'
    }

    def __init__(self,
                 id=None,
                 code=None,
                 status=None,
                 created_at=None,
                 customer=None):
        """Constructor for the GetAccessTokenResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.customer = customer


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        code = dictionary.get('code')
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        customer = pagarmecoreapi.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None

        # Return an object of this model
        return cls(id,
                   code,
                   status,
                   created_at,
                   customer)

