# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.create_customer_request
import pagarmecoreapi.models.create_payment_request
import pagarmecoreapi.models.create_antifraud_request

class CreateChargeRequest(object):

    """Implementation of the 'CreateChargeRequest' model.

    Request for creating a new charge

    Attributes:
        code (string): Code
        amount (int): The amount of the charge, in cents
        customer_id (string): The customer's id
        customer (CreateCustomerRequest): Request for creating a new customer
        payment (CreatePaymentRequest): Payment data
        metadata (dict<object, string>): Metadata
        due_at (datetime): The charge due date
        antifraud (CreateAntifraudRequest): TODO: type description here.
        order_id (string): Order Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "amount":'amount',
        "customer_id":'customer_id',
        "customer":'customer',
        "payment":'payment',
        "metadata":'metadata',
        "antifraud":'antifraud',
        "order_id":'order_id',
        "due_at":'due_at'
    }

    def __init__(self,
                 code=None,
                 amount=None,
                 customer_id=None,
                 customer=None,
                 payment=None,
                 metadata=None,
                 antifraud=None,
                 order_id=None,
                 due_at=None):
        """Constructor for the CreateChargeRequest class"""

        # Initialize members of the class
        self.code = code
        self.amount = amount
        self.customer_id = customer_id
        self.customer = customer
        self.payment = payment
        self.metadata = metadata
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None
        self.antifraud = antifraud
        self.order_id = order_id


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
        code = dictionary.get('code')
        amount = dictionary.get('amount')
        customer_id = dictionary.get('customer_id')
        customer = pagarmecoreapi.models.create_customer_request.CreateCustomerRequest.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        payment = pagarmecoreapi.models.create_payment_request.CreatePaymentRequest.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        metadata = dictionary.get('metadata')
        antifraud = pagarmecoreapi.models.create_antifraud_request.CreateAntifraudRequest.from_dictionary(dictionary.get('antifraud')) if dictionary.get('antifraud') else None
        order_id = dictionary.get('order_id')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None

        # Return an object of this model
        return cls(code,
                   amount,
                   customer_id,
                   customer,
                   payment,
                   metadata,
                   antifraud,
                   order_id,
                   due_at)


