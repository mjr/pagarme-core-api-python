# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_card_request

class CreateVoucherPaymentRequest(object):

    """Implementation of the 'CreateVoucherPaymentRequest' model.

    The settings for creating a voucher payment

    Attributes:
        statement_descriptor (string): The text that will be shown on the
            voucher's statement
        card_id (string): Card id
        card_token (string): Card token
        card (CreateCardRequest): Card info

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor":'statement_descriptor',
        "card_id":'card_id',
        "card_token":'card_token',
        "card":'Card'
    }

    def __init__(self,
                 statement_descriptor=None,
                 card_id=None,
                 card_token=None,
                 card=None):
        """Constructor for the CreateVoucherPaymentRequest class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.card_id = card_id
        self.card_token = card_token
        self.card = card


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
        statement_descriptor = dictionary.get('statement_descriptor')
        card_id = dictionary.get('card_id')
        card_token = dictionary.get('card_token')
        card = pagarmecoreapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get('Card')) if dictionary.get('Card') else None

        # Return an object of this model
        return cls(statement_descriptor,
                   card_id,
                   card_token,
                   card)

