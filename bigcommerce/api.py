from bigcommerce.connection import Connection


class BigCommerceApi:
    def __init__(self, path: str, client_id: str, access_token: str):
        """
        Initialize BigCommerce API client from Pydantic config.

        :param config: BigCommerceConfig instance
        """
        self.client = Connection(path, client_id, access_token)

    def get(self, resource: str, params: dict | None = None):
        """
        Execute a GET request against the BigCommerce API.

        :param resource: API endpoint or resource path
        :param params: Query parameters to include in the request
        :return: The response from the Connection.run call
        """
        return self.client.run_method("GET", resource, params=params)

    def put(self, resource: str, params: dict, data: dict):
        """
        Execute a GET request against the BigCommerce API.

        :param resource: API endpoint or resource path
        :param params: Query parameters to include in the request
        :return: The response from the Connection.run call
        """
        return self.client.run_method("GET", resource, params=params)
