import json
from .baseclient import BaseClient
from .models import TrainingJob

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class TrainingModel(BaseClient):

    def __init__(self, access_token):
        BaseClient.__init__(self, access_token)

    def submit_job_training(self, filename, model_name):
        if not filename:
            raise ValueError('Filename must be provided')
        payload = {'model_name': model_name}
        with open(filename, 'rb') as f:
            files = {
                'file': (filename, f)
            }
            response = self._make_http_request(
                "POST",
                urljoin(self.base_url, 'job'),
                files=files, data=payload
            )

        return response.json()

    def get_job_training_details(self, job_id):
        if not job_id:
            raise ValueError('id_ must be provided')
        payload = {'job_id':job_id}
        response = self._make_http_request(
            "POST",
            urljoin(self.base_url, 'train-status'),
            json=payload
        )
        return response.json()

    def get_list_of_models(self):
        response = self._make_http_request(
            "GET",
            urljoin(self.base_url, 'get-model-list')
        )
        return response.json()
