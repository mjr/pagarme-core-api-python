# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_split_options_request

class CancelSplitRequest(object):

    """Implementation of the 'CancelSplitRequest' model.

    Split

    Attributes:
        mtype (string): Split type
        amount (int): Amount
        recipient_id (string): Recipient id
        options (CreateSplitOptionsRequest): The split options request
        split_rule_id (string): Rule id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "amount":'amount',
        "recipient_id":'recipient_id',
        "options":'options',
        "split_rule_id":'Split_Rule_ID'
    }

    def __init__(self,
                 mtype=None,
                 amount=None,
                 recipient_id=None,
                 options=None,
                 split_rule_id=None):
        """Constructor for the CancelSplitRequest class"""

        # Initialize members of the class
        self.mtype = mtype
        self.amount = amount
        self.recipient_id = recipient_id
        self.options = options
        self.split_rule_id = split_rule_id


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
        mtype = dictionary.get('type')
        amount = dictionary.get('amount')
        recipient_id = dictionary.get('recipient_id')
        options = pagarmecoreapi.models.create_split_options_request.CreateSplitOptionsRequest.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None
        split_rule_id = dictionary.get('Split_Rule_ID')

        # Return an object of this model
        return cls(mtype,
                   amount,
                   recipient_id,
                   options,
                   split_rule_id)

