from typing import Any
import requests


class Connection:
    def __init__(self, path: str, client_id: str, access_token: str):
        """
        Initialize BigCommerce connection.

        :param config: BigCommerceConfig instance
        :param api_path: Base URL for BigCommerce API (e.g., v3 base URL)
        """
        self.path = path.rstrip('/')
        self.session = requests.Session()
        # Attach authentication headers to all requests
        self.session.headers.update(self.get_headers(client_id, access_token))

    @staticmethod
    def get_headers(client_id: str, access_token: str) -> dict:
        """
        Return default headers for BigCommerce API calls.
        """
        return {'X-Auth-Client': client_id, 'X-Auth-Token': access_token}

    def run_method(
        self,
        method: str,
        resource: str,
        params: dict | None = None,
        data: dict | None = None,
    ) -> Any:
        """
        Execute HTTP request and return parsed JSON or handle errors.

        :param method: HTTP method (GET, POST, PUT, DELETE)
        :param endpoint: API endpoint path (appended to base path)
        :param kwargs: Additional request arguments (params, json, headers, etc.)
        :return: Parsed JSON response
        """
        url = f"{self.path}/{resource.lstrip('/')}"
        response = self.session.request(method, url, params=params, json=data)
        return self.error_handler(response)

    @staticmethod
    def error_handler(response: requests.Response) -> Any:
        """
        Handle HTTP errors or return JSON body.

        :param response: requests.Response object
        :return: JSON-decoded response if OK
        :raises: HTTPError if the response status is 4xx/5xx
        """
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            # Customize error handling as needed
            raise e
        return response.json()

    def __del__(self):
        """
        Destructor to ensure HTTP session is closed.
        """
        try:
            self.session.close()
        except Exception:
            pass
