"""
server.py

This module provides a Flask web application for emotion detection
using a pre-defined emotion analysis model. It includes endpoints 
to analyze text for emotional content and render the index page.
"""

from flask import Flask, request,jsonify,render_template  # Import request for handling requests
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def emotion_analyzer():
    """
    Analyzes the provided text for emotional content.

    Retrieves the text to analyze from the request arguments and
    returns a formatted string with the emotion scores and the
    dominant emotion.

    Returns:
        str: Formatted response string containing emotion analysis.
    """
    # Get the input text from the query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if the input text is provided
    if not text_to_analyze:
        return jsonify({"error": " Invalid text! Please try again!."}), 400

    # Get emotion analysis result
    emotions = emotion_detector(text_to_analyze)

    # Return the result in the specified format
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_message

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
