import json
import requests

def emotion_detector(text_to_analyze):
    watson_url = ("https://sn-watson-emotion.labs.skills.network/"
                  + "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
    watson_headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {"text": text_to_analyze} 
    }
    # call Watson emotion analyzer
    response = requests.post(watson_url,
                             json=input_json,
                             headers=watson_headers,
                             timeout=5000)
    # check for error
    if response.status_code == 400:
        emotion_dict = {"anger": None, "disgust": None, "fear": None,
                        "joy": None, "sadness": None, "dominant_emotion": None}
    else:
        # convert response to dict and extract required data
        response_dict = json.loads(response.text)
        emotion_dict = response_dict["emotionPredictions"][0]["emotion"]
        # determine "dominant emotion"
        dominant_emotion = max(emotion_dict.items(),
                            key=lambda epair: epair[1])[0]
        emotion_dict["dominant_emotion"] = dominant_emotion
    return emotion_dict
