from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_api():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_analysis = emotion_detector(text_to_analyze)
    response_string = (
        "For the given statement, the system response is "
        + f"'anger': {emotion_analysis['anger']}, "
        + f"'disgust': {emotion_analysis['disgust']}, "
        + f"'fear': {emotion_analysis['fear']}, "
        + f"'joy': {emotion_analysis['joy']} and "
        + f"'sadness': {emotion_analysis['sadness']}. "
        + "The dominant emotion is "
        + f"<b>{emotion_analysis['dominant_emotion']}</b>."
    )
    return response_string


@app.route("/")
def display_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
