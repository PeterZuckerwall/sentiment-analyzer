import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬")
st.title("💬 Sentiment Analyzer")
st.write("Enter a sentence and get the predicted sentiment using a pretrained Hugging Face model.")

@st.cache_resource
def load_model():
    try:
        return pipeline("sentiment-analysis")
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None  

sentiment_model = load_model()


text = st.text_area("Enter text here:", placeholder="Type something like 'I love this product!'")

if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    elif sentiment_model is None:
        st.error("❌ Sentiment model could not be loaded. Please check your setup.")
    else:
        result = sentiment_model(text)[0]
        label = result["label"]
        score = result["score"]
        emoji = "😄" if label == "POSITIVE" else "☹️"
        st.success(f"{emoji} **{label}** ({score * 100:.2f}%)")
