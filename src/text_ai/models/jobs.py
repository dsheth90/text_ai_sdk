from .job_status import JobStatus


class Job:
    def __init__(self, job_id):
        self.job_id = job_id

    @classmethod
    def from_json(cls, json):
        return json['job_id']
