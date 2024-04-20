import json
from shopify import Customer
from Shopify_connection.utils.session_shopify import create_session, clear_shopify_session


def find_customers(customers_json: json) -> list[Customer]:
    """
    Find customers by ID from a JSON string.
    :param: customers_json: A JSON string containing customer IDs.
    :return: A list of Customer objects.
    :raises: ValueError: If the customers_json is invalid or
    the customers are not found.
    """
    if customers_json is None or not isinstance(customers_json, str):
        raise ValueError("Invalid customers_json")

    try:
        customer_ids = [customer['id'] for customer in json.loads(customers_json)]
    except (json.JSONDecodeError, KeyError):
        raise ValueError("Invalid JSON format")

    create_session()

    customers = [Customer.find(customer_id) for customer_id in customer_ids]

    if any(customer is None for customer in customers):
        raise ValueError("One or more customers not found")

    clear_shopify_session()

    return customers
