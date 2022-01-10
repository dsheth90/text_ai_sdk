class ApiCount:
    def __init__(self,
                 api_calls_count,
                 model_training=None,
                 model_training_details=None,
                 model_list=None,
                 prediction_text=None,
                 prediction_file=None,
                 prediction_details=None,
                 list_of_jobs=None,
                 sentiment_result=None,
                 model_wise_sentiment_result=None,
                 general_sentiment_result=None):

        self.api_calls_count = api_calls_count
        self.model_training = model_training
        self.model_training_details = model_training_details
        self.model_list = model_list
        self.prediction_text = prediction_text
        self.prediction_file = prediction_file
        self.prediction_details = prediction_details
        self.list_of_jobs = list_of_jobs
        self.sentiment_result = sentiment_result
        self.model_wise_sentiment_result = model_wise_sentiment_result
        self. general_sentiment_result = general_sentiment_result

    @classmethod
    def from_json(cls, json):
        return cls(
            json['api_calls_count'],
            json.get('model_training'),
            json.get('model_training_details'),
            json.get('model_list'),
            json.get('prediction_text'),
            json.get('prediction_file'),
            json.get('prediction_details'),
            json.get('list_of_jobs'),
            json.get('sentiment_result'),
            json.get('model_wise_sentiment_result'),
            json.get('general_sentiment_result')
        )
