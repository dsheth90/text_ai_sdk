from text_ai import apiclient, trainingapiclient, statsapiclient

client = apiclient.TextAiAPIClient("235c0daf-96dd-4d1a-b5a7-a6a75054fcd8")

# Result - /get-result
# print(client.get_sentiment_json("8e8a6d89-9af5-497c-9ce1-25df6b94b663"))


# Prediction - /predict
data = {
    "model_name":"test3",
    "model_type":"Custom",
    "text": [
                {
                    "text": "i am updating my blog because i feel shitty",
                    "text_id": 1
                },
                {
                    "text": "i find myself in the odd position of feeling supportive of",
                    "text_id": 2
                },
                {
                    "text": "i feel like i m defective or something for not having baby fever",
                    "text_id": 3
                },
                {
                    "text": "im feeling insecure at the moment",
                    "text_id": 4
                },
                {
                    "text": "i know its easy to feel a little envious of me and i cant tell you that you shouldnt",
                    "text_id": 5
                }
            ]
}
# print(client.submit_job_text(data['text'], data['model_name'], data['model_type']))


# StatusTask - /task-status
# print(client.get_job_details("bf71d779-c117-419f-b3a4-490a75833da2"))


# Prediction FIle - /prediction-file
# print(client.submit_job_file('/Users/dhrumilsheth/Desktop/Project/Sentiment/text-ai-celery-sample/training_file/api_testing.csv', 'test3', 'Custom'))


# TaskDateFilter - /get-task
# data = client.get_list_of_jobs('2022-01-01', '2022-01-09')
# print(len(data['tasks']))

client1 = trainingapiclient.TrainingModel("235c0daf-96dd-4d1a-b5a7-a6a75054fcd8")

# JobTask - /job
# print(client1.submit_job_training('/Users/dhrumilsheth/Desktop/Project/Sentiment/text-ai-celery-sample/training_file/training_data.csv', 'test7'))

# StatusTrain - /train-status
# print(client1.get_job_training_details("1a01467e-89f9-401b-be73-c9c961c8f66f"))

# UserModelList - /get-model-list
# print(client1.get_list_of_models())


client2 = statsapiclient.Statistics("235c0daf-96dd-4d1a-b5a7-a6a75054fcd8")

# ModelWiseResult - /get-result-model
# print(client2.get_sentiment_stats_modelwise())

# OverallResult - /get-result-overall
# print(client2.get_sentiment_stats())

# DateWiseModelResult - /get-range-model-result
print(client2.get_datewise_result_model('2022-01-01', '2022-01-9'))

# DateWiseOverallResult - /get-range-result
print(client2.get_datewise_result('2022-01-01', '2022-01-9'))
