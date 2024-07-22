'''Flask Server'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detect():
    '''Response emotion detected in the text'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    response = ""
    if dominant_emotion :
        response = f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
        The dominant emotion is {dominant_emotion}."
    else :
        response = "Invalid text! Please try again!"

    return response


@app.route("/")
def render_index_page():
    '''Return static page'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
