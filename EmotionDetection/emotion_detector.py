import requests
import json

def emotion_detector(text_to_analyze):
    # API URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        # Send the POST request
        response = requests.post(url, json=myobj, headers=header)

        # Check the response status code
        if response.status_code == 200:
            # Convert the response text into a dictionary
            response_dict = json.loads(response.text)

            # Extract emotion predictions from the response
            emotions = response_dict['emotionPredictions'][0]['emotion']

            # Extract individual emotion scores
            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)

            # Find the dominant emotion
            emotion_scores = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return the final dictionary with emotion scores and dominant emotion
            result = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }

            return result
        
        # Handle specific error codes
        elif response.status_code == 400:
            return {'error': 'Bad request. Please check your input.'}
        elif response.status_code == 500:
            return {'error': 'Internal server error. Please try again later.'}
        else:
            return {'error': f'Unexpected error occurred: {response.status_code}'}

    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
