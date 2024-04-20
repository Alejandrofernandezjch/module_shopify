from shopify import Session, ShopifyResource

shop_name = "tu-tienda-shopify.com",
api_key = "tu-clave-api",
password = "tu-contraseña-administrador"


def create_session():
    # Create a session
    session = Session(shop_name, api_key, password)
    # Activate the session
    shop = ShopifyResource.activate_session(session)
    return shop


def clear_shopify_session():
    """
    Clear the active Shopify session.
    :return: ShopifyResource
    :raises: ValueError if there is no active Shopify session to clear
    """
    if ShopifyResource.site is None or ShopifyResource.myshopify_domain is None:
        raise ValueError("No active Shopify session to clear")

    return ShopifyResource.clear_session()


