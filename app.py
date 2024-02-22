from flask import Flask, request, jsonify
import logging
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Setting up logging
logging.basicConfig(filename='api.log', level=logging.INFO)

def sentiment(sentence):
    """
    Perform sentiment analysis on the input sentence using NLTK's Vader lexicon.

    Args:
        sentence (str): The input text for sentiment analysis.

    Returns:
        str: The sentiment label ('Positive', 'Negative', or 'Neutral').
    """    
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)['compound']
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def sentiment_request():

    """
    Endpoint for performing sentiment analysis.

    - Accepts GET and POST requests.
    - Expects 'q' parameter with the text to analyze.
    - Returns JSON response with the sentiment label.

    Returns:
        JSON: Response containing the sentiment label.
    """
    if request.method == "POST":
        sentence = request.form.get('q')
    else:
        sentence = request.args.get('q')

    if not sentence:
        # Handling invalid input
        logging.error("Invalid input: No text provided.")
        return jsonify({"error": "No text provided."}), 400

    try:
        sent = sentiment(sentence)
        output = {'sentiment': sent}
        logging.info(f"Input: {sentence}, Sentiment: {sent}")
        return jsonify(output)
    except Exception as e:
        # Handling server errors
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
