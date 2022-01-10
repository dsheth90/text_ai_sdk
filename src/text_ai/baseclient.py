import requests
from requests.exceptions import HTTPError
from . import __version__


class BaseClient:
    base_url = 'http://127.0.0.1:5000/'

    def __init__(self, access_token):
        if not access_token:
            raise ValueError('Access token must be provided')
        self.default_headers = {
            'SDK_Authorization': 'Bearer {}'.format(access_token)
        }

    def _make_http_request(self, method, url, **kwargs):

        headers = self.default_headers.copy()
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        with requests.session() as session:
            response = session.request(method, url, headers=headers, **kwargs)

        try:
            response.raise_for_status()
            return response
        except HTTPError as err:
            if (response.content):
                err.args = (err.args[0] +
                            "; Server Response : {}".
                            format(response.content.decode('utf-8')),)
            raise
