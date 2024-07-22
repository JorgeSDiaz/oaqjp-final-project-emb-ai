import requests
import json


def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text } }
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)

    response_emotions = {}

    if response.status_code == 200:
        emotions_scores = formatted_response["emotionPredictions"][0]["emotion"]

        response_emotions = {
            'anger': emotions_scores["anger"],
            'disgust': emotions_scores["disgust"],
            'fear': emotions_scores["fear"],
            'joy': emotions_scores["joy"],
            'sadness': emotions_scores["sadness"]
        }

        response_emotions.update({'dominant_emotion': max(response_emotions, key=response_emotions.get)})
    elif response.status_code == 400:
        response_emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return response_emotions