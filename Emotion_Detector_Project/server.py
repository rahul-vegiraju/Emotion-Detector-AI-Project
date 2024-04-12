"""
This module implements a Flask server for emotion detection.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects emotion in the provided text.

    Returns:
        JSON response containing emotion analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        response = emotion_detector(text_to_analyze)
        if response is not None:
            return jsonify(response)
    return "Invalid input! Try again."

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.

    Returns:
        Rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    