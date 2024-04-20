from shopify import Customer
from Shopify_connection.utils.session_shopify import create_session, clear_shopify_session


def get_customers() -> list[Customer]:
    """
    Get all customers from the Shopify store.
    :return: A list of Customer objects.
    :raises: ValueError if the customers are not found or
    the Shopify session cannot be created.
    """

    session = create_session()

    if session is None:
        raise ValueError("Failed to create a Shopify session")

    customers = Customer.find()

    if customers is None:
        raise ValueError("Failed to fetch customers")

    session_clear = clear_shopify_session()

    if session_clear.site is not None:
        raise ValueError("Failed to clear the Shopify session")

    return customers
