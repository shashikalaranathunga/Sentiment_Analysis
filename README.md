# Sentiment Analysis Flask API
This sentiment analysis API allows you to get Sentiment for a sentence using GET and POST methods.

## Requirements
Use these or any latest  version if you already have installed.\
    Flask==3.0.2
    nltk==3.8.1

## Setup 

1. Clone the repository:
    git clone https://github.com/your_username/sentiment-analysis-flask-api.git](https://github.com/shashikalaranathunga/Sentiment_Analysis.git
2. Navigate to the project directory:
    cd sentiment-analysis-flask-api
3. Install dependencies:
    pip install -r requirements.txt
4. Run the Flask server:
    flask run


## Usage
Using GET method - 

    http://127.0.0.1:5000?q="Text String to check Sentiment."
Using POST method - 

    curl http://127.0.0.1:5000 -d "q='Text String to check Sentiment.'"
or use in a web based form and send POST request.
## Output
Output is JSON based which is as follows -

    {"sentiment":"Negative"}
or

    {"sentiment":"Positive"}

or 
     {"sentiment":"neutral"}

