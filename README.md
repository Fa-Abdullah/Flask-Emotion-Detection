# Flask Emotion Detection

A Flask-based web application that analyzes the emotional tone of user-provided text using the IBM Watson NLP Emotion Prediction API. The application detects five core emotions and identifies the dominant emotion in the input text.

## Features

* Emotion detection from English text
* Detects five emotions:

  * Anger
  * Disgust
  * Fear
  * Joy
  * Sadness
* Identifies the dominant emotion
* REST API built with Flask
* Input validation and error handling
* Simple web interface using HTML templates

## Project Structure

```text
Flask-Emotion-Detection/
│
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│   └── test_emotion_detection.py
│
├── templates/
│   └── index.html
│
├── server.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Flask
* Requests
* IBM Watson NLP Emotion Prediction API

## How It Works

1. The user enters a text statement.
2. Flask receives the request.
3. The application sends the text to the IBM Watson Emotion Prediction API.
4. The API returns confidence scores for:

   * Anger
   * Disgust
   * Fear
   * Joy
   * Sadness
5. The application determines the dominant emotion.
6. The formatted response is returned to the user.

## Installation

Clone the repository

```bash
git clone https://github.com/Fa-Abdullah/Flask-Emotion-Detection.git
cd Flask-Emotion-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python server.py
```

The application will start on:

```text
http://localhost:5001
```

## API Endpoint

### Analyze Emotion

**POST**

```text
/emotionDetector
```

### Request

```json
{
    "text": "I am very happy today!"
}
```

### Example Response

```text
For the given statement, the system response is
'anger': 0.01,
'disgust': 0.02,
'fear': 0.01,
'joy': 0.93 and
'sadness': 0.03.
The dominant emotion is joy.
```

## Error Handling

The application handles:

* Invalid JSON requests
* Missing input text
* API connection failures
* Invalid API responses
* Unexpected server exceptions

