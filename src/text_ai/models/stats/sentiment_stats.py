class SentimentCount:
    def __init__(self,
                 Happy,
                 Sad,
                 Angry,
                 Fear,
                 Neutral,
                 model_id=None):

        self.Happy = Happy
        self.Sad = Sad
        self.Angry = Angry
        self.Fear = Fear
        self.Neutral = Neutral
        self.model_id = model_id

    @classmethod
    def from_json(cls, json):
        return cls(
            json['Happy'],
            json['Sad'],
            json['Angry'],
            json['Fear'],
            json['Neutral'],
            json.get('model_id')
        )
