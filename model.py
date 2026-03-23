from transformers import pipeline
from langdetect import detect
from deep_translator import GoogleTranslator

# 🔍 Sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 🌍 Language detect
def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

# 🔄 Translate to English
def to_english(text, lang):
    if lang == "en":
        return text
    try:
        return GoogleTranslator(source=lang, target="en").translate(text)
    except:
        return text

# 🔄 Translate back
def from_english(text, lang):
    if lang == "en":
        return text
    try:
        return GoogleTranslator(source="en", target=lang).translate(text)
    except:
        return text

# 🧠 Sentiment detect
def detect_sentiment(text):
    result = sentiment_model(text)[0]['label']
    return "positive" if result == "POSITIVE" else "negative"

# 🤖 Chatbot
def chatbot(query):
    
    # 🌍 Detect language
    lang = detect_language(query)
    
    # 🔄 Convert to English
    query_en = to_english(query, lang)

    # 🧠 Sentiment
    sentiment = detect_sentiment(query_en)

    # 🎯 Response logic
    if sentiment == "positive":
        response_en = f"😊 Great! I'm glad you're interested. Let me explain: {query_en}"
    else:
        response_en = f"😔 I understand it feels difficult. Don't worry, I'll help you: {query_en}"

    # 🔄 Convert back
    final_response = from_english(response_en, lang)

    return final_response, sentiment, lang