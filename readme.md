# Sentiment Analyzer (Version 1 - Local)

A simple sentiment analysis app built with Python, Streamlit, and a Hugging Face model (TensorFlow backend).

##  How to Run

1. Create a virtual environment (optional but recommended)
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run sentiment_app.py`


- Takes user input
- Uses a pretrained BERT-based model from Hugging Face
- Displays whether the sentiment is POSITIVE or NEGATIVE, with confidence

##  Model

Uses `distilbert-base-uncased-finetuned-sst-2-english` via `transformers.pipeline()`
