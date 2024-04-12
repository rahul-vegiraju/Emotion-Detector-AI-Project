import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json()  # Parse response JSON
        
        # Check if the expaected structure is present in the response
        if 'emotion_predictions' in data:
            emotion_predictions = data['emotion_predictions']
        elif 'emotionPredictions' in data:
            emotion_predictions = data['emotionPredictions']
        else:
            print("Unexpected response format:")
            print(data)
            return None
        
        # Extract required emotions and their scores
        emotions = {
            'anger': emotion_predictions[0]['emotion']['anger'],
            'disgust': emotion_predictions[0]['emotion']['disgust'],
            'fear': emotion_predictions[0]['emotion']['fear'],
            'joy': emotion_predictions[0]['emotion']['joy'],
            'sadness': emotion_predictions[0]['emotion']['sadness']
        }

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Prepare the output dictionary
        output = {
            "anger": emotions['anger'],
            "disgust": emotions['disgust'],
            "fear": emotions['fear'],
            "joy": emotions['joy'],
            "sadness": emotions['sadness'],
            "dominant_emotion": dominant_emotion
        }

        return output
        
    except requests.exceptions.RequestException as e:
        # Handle HTTP errors
        print("Error:", e)
        return None
