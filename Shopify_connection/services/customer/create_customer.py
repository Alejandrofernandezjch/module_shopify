import json
from shopify import Customer
from Shopify_connection.utils.session_shopify import create_session, clear_shopify_session


def create_customer(customers_json: json) -> Customer:
    """
    Create a new customer in the Shopify store from a JSON file.
    :param : The path to the JSON file containing the customer details.
    :return: The created Customer object.
    :raises: ValueError if the customer cannot be created or
    the Shopify session cannot be created.
    """

    # Load the customer details from the JSON file
    with open(customers_json, 'r') as file:
        customer_details = json.load(file)

    if not all([customer_details.get('first_name'), customer_details.get('last_name'), customer_details.get('email')]):
        raise ValueError("All parameters are required")

    session = create_session()

    if session is None:
        raise ValueError("Failed to create a Shopify session")

    new_customer = Customer()
    new_customer.first_name = customer_details['first_name']
    new_customer.last_name = customer_details['last_name']
    new_customer.email = customer_details['email']

    if not new_customer.save():
        raise ValueError("Failed to create the customer")

    clear_shopify_session()

    return new_customer
