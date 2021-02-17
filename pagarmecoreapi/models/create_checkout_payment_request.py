# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_checkout_credit_card_payment_request
import pagarmecoreapi.models.create_checkout_debit_card_payment_request
import pagarmecoreapi.models.create_checkout_boleto_payment_request
import pagarmecoreapi.models.create_address_request
import pagarmecoreapi.models.create_checkout_bank_transfer_request

class CreateCheckoutPaymentRequest(object):

    """Implementation of the 'CreateCheckoutPaymentRequest' model.

    Checkout payment request

    Attributes:
        accepted_payment_methods (list of string): Accepted Payment Methods
        accepted_multi_payment_methods (list of object): Accepted Multi
            Payment Methods
        success_url (string): Success url
        default_payment_method (string): Default payment method
        gateway_affiliation_id (string): Gateway Affiliation Id
        credit_card (CreateCheckoutCreditCardPaymentRequest): Credit Card
            payment request
        debit_card (CreateCheckoutDebitCardPaymentRequest): Debit Card payment
            request
        boleto (CreateCheckoutBoletoPaymentRequest): Boleto payment request
        customer_editable (bool): Customer is editable?
        expires_in (int): Time in minutes for expiration
        skip_checkout_success_page (bool): Skip postpay success screen?
        billing_address_editable (bool): Billing Address is editable?
        billing_address (CreateAddressRequest): Billing Address
        bank_transfer (CreateCheckoutBankTransferRequest): Bank Transfer
            payment request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accepted_payment_methods":'accepted_payment_methods',
        "accepted_multi_payment_methods":'accepted_multi_payment_methods',
        "success_url":'success_url',
        "skip_checkout_success_page":'skip_checkout_success_page',
        "billing_address_editable":'billing_address_editable',
        "billing_address":'billing_address',
        "bank_transfer":'bank_transfer',
        "default_payment_method":'default_payment_method',
        "gateway_affiliation_id":'gateway_affiliation_id',
        "credit_card":'credit_card',
        "debit_card":'debit_card',
        "boleto":'boleto',
        "customer_editable":'customer_editable',
        "expires_in":'expires_in'
    }

    def __init__(self,
                 accepted_payment_methods=None,
                 accepted_multi_payment_methods=None,
                 success_url=None,
                 skip_checkout_success_page=None,
                 billing_address_editable=None,
                 billing_address=None,
                 bank_transfer=None,
                 default_payment_method=None,
                 gateway_affiliation_id=None,
                 credit_card=None,
                 debit_card=None,
                 boleto=None,
                 customer_editable=None,
                 expires_in=None):
        """Constructor for the CreateCheckoutPaymentRequest class"""

        # Initialize members of the class
        self.accepted_payment_methods = accepted_payment_methods
        self.accepted_multi_payment_methods = accepted_multi_payment_methods
        self.success_url = success_url
        self.default_payment_method = default_payment_method
        self.gateway_affiliation_id = gateway_affiliation_id
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.boleto = boleto
        self.customer_editable = customer_editable
        self.expires_in = expires_in
        self.skip_checkout_success_page = skip_checkout_success_page
        self.billing_address_editable = billing_address_editable
        self.billing_address = billing_address
        self.bank_transfer = bank_transfer


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
        accepted_payment_methods = dictionary.get('accepted_payment_methods')
        accepted_multi_payment_methods = dictionary.get('accepted_multi_payment_methods')
        success_url = dictionary.get('success_url')
        skip_checkout_success_page = dictionary.get('skip_checkout_success_page')
        billing_address_editable = dictionary.get('billing_address_editable')
        billing_address = pagarmecoreapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        bank_transfer = pagarmecoreapi.models.create_checkout_bank_transfer_request.CreateCheckoutBankTransferRequest.from_dictionary(dictionary.get('bank_transfer')) if dictionary.get('bank_transfer') else None
        default_payment_method = dictionary.get('default_payment_method')
        gateway_affiliation_id = dictionary.get('gateway_affiliation_id')
        credit_card = pagarmecoreapi.models.create_checkout_credit_card_payment_request.CreateCheckoutCreditCardPaymentRequest.from_dictionary(dictionary.get('credit_card')) if dictionary.get('credit_card') else None
        debit_card = pagarmecoreapi.models.create_checkout_debit_card_payment_request.CreateCheckoutDebitCardPaymentRequest.from_dictionary(dictionary.get('debit_card')) if dictionary.get('debit_card') else None
        boleto = pagarmecoreapi.models.create_checkout_boleto_payment_request.CreateCheckoutBoletoPaymentRequest.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        customer_editable = dictionary.get('customer_editable')
        expires_in = dictionary.get('expires_in')

        # Return an object of this model
        return cls(accepted_payment_methods,
                   accepted_multi_payment_methods,
                   success_url,
                   skip_checkout_success_page,
                   billing_address_editable,
                   billing_address,
                   bank_transfer,
                   default_payment_method,
                   gateway_affiliation_id,
                   credit_card,
                   debit_card,
                   boleto,
                   customer_editable,
                   expires_in)

