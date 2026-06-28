import requests
import json

# from emotion_detection import emotion_detector
# emotion_detector(" I am so happy I am doing this.")

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        return {"error": "Error connecting to the API"}

    # Print the raw response for debugging
    #print("Response Status Code:", response.status_code)
    #print("Response Text:", response.text)

    if response.status_code != 200:
        print("API request failed with status code:", response.status_code)
        return {"error": f"API request failed with status code {response.status_code}"}

    try:
        response_dict = json.loads(response.text)
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        return {"error": "Failed to decode JSON response"}

    # Debugging the response structure
    print("Response Dictionary:", response_dict)

    # Accessing the 'emotionPredictions' key
    emotions_list = response_dict.get('emotionPredictions', [])
    print("Emotions List:", emotions_list)  # Debugging the emotions data

    if isinstance(emotions_list, list) and len(emotions_list) > 0:
        # Assuming the first element contains the emotion scores
        emotion_data = emotions_list[0]
        emotion = emotion_data.get('emotion', {})
        anger_score = emotion.get('anger', 0)
        disgust_score = emotion.get('disgust', 0)
        fear_score = emotion.get('fear', 0)
        joy_score = emotion.get('joy', 0)
        sadness_score = emotion.get('sadness', 0)
    else:
        print("No valid emotions detected.")
        return {"error": "No valid emotions detected"}

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }