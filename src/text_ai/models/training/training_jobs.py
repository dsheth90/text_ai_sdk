from ..job_status import JobStatus


class TrainingJob:
    def __init__(self, _id, model_id, model_name, created_on, status,
                 completed_on=None, error_message=None,
                 execution_time=None):
        self.id = _id
        self.model_id = model_id
        self.model_name = model_name
        self.created_on = created_on
        self.completed_on = completed_on
        self.status = status
        self.error_message = error_message
        self.execution_time = execution_time

    @classmethod
    def from_json(cls, json):
        return cls(
            json['id'],
            json['model_id'],
            json['model_name'],
            json['created_on'],
            JobStatus.from_string(json['status']),
            json.get('completed_on'),
            json.get('error_message'),
            json.get('execution_time')
        )
