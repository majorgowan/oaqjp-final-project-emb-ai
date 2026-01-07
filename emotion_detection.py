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

    response = requests.post(watson_url,
                             json=input_json,
                             headers=watson_headers,
                             timeout=5000)
    return response.text
