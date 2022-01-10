import json
from .baseclient import BaseClient
from .models import Job

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class TextAiAPIClient(BaseClient):

    def __init__(self, access_token):
        BaseClient.__init__(self, access_token)

    def submit_job_text(self, text, model_name, model_type):
        if not text:
            raise ValueError('Text should not be empty')
        payload = {'text': text, 'model_name': model_name, 'model_type':model_type}
        response = self._make_http_request("POST", urljoin(self.base_url, 'predict'),
                                           json=payload)
        return response.json()

    def submit_job_file(self, filename, model_name, model_type):
        if not filename:
            raise ValueError('Filename must be provided')
        payload = {'model_type': model_type, 'model_name':model_name}
        with open(filename, 'rb') as f:
            files = {
                    'text': (filename, f)
                    }
            response = self._make_http_request(
                "POST",
                urljoin(self.base_url, 'prediction-file'),
                files=files, data=payload
            )

        return response.json()

    def get_job_details(self, job_id):
        if not job_id:
            raise ValueError('id_ must be provided')
        payload = {'job_id': job_id}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'task-status'), json=payload
        )
        return response.json()

    def get_list_of_jobs(self, start_date, end_date):
        payload = {'start_date': start_date, 'end_date': end_date}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'get-task'),
            json=payload
        )
        return response.json()

    def get_sentiment_json(self, job_id):
        if not job_id:
            raise ValueError('id_ must be provided')
        payload = {'job_id':job_id}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'get-result'), json=payload
        )

        return response.json()
