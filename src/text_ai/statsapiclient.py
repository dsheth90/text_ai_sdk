from .baseclient import BaseClient
from .models import ApiCount, SentimentCount

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class Statistics(BaseClient):

    def __init__(self, access_token):
        BaseClient.__init__(self, access_token)

    def get_api_call_count(self):
        response = self._make_http_request(
            "GET",
            urljoin(self.base_url, 'api-count')
        )

        return ApiCount.from_json(response.json())

    def get_sentiment_stats_modelwise(self):
        response = self._make_http_request(
            "GET",
            urljoin(self.base_url, 'get-result-model')
        )
        return response.json()

    def get_sentiment_stats(self):
        response = self._make_http_request(
            "GET",
            urljoin(self.base_url, 'get-result-overall')
        )
        return response.json()

    def get_datewise_result_model(self, start_date, end_date):
        payload = {'start_date': start_date, 'end_date': end_date}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'get-range-model-result'),
            json=payload
        )
        return response.json()

    def get_datewise_result(self, start_date, end_date):
        payload = {'start_date': start_date, 'end_date': end_date}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'get-range-result'),
            json=payload
        )
        return response.json()
