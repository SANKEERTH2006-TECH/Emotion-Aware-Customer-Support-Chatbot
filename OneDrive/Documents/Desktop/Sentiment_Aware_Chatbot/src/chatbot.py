"""
==========================================
Emotion-Aware Customer Support Chatbot
Main Chatbot Controller
==========================================
"""

from src.sentiment import detect_sentiment
from src.response_generator import generate_response
from src.memory import (
    add_to_memory,
    get_history,
    get_history_list,
    clear_memory,
    get_total_messages
)

from src.utils import (
    clean_text,
    response_quality
)


# ==========================================
# Analytics Storage
# ==========================================

analytics = {

    "Positive": 0,
    "Neutral": 0,
    "Negative": 0,

    "Joy": 0,
    "Anger": 0,
    "Sadness": 0,
    "Fear": 0,
    "Surprise": 0,
    "NeutralEmotion": 0
}


# ==========================================
# Update Analytics
# ==========================================

def update_analytics(sentiment, emotion):

    if sentiment in analytics:
        analytics[sentiment] += 1

    if emotion in analytics:
        analytics[emotion] += 1


# ==========================================
# Main Chat Function
# ==========================================

def chat(user_message):

    user_message = clean_text(user_message)

    if len(user_message) == 0:

        return {

            "response": "Please enter a message.",

            "sentiment": "Neutral",

            "emotion": "NeutralEmotion",

            "confidence": 0
        }

    # --------------------------------------

    sentiment_result = detect_sentiment(user_message)

    sentiment = sentiment_result["sentiment"]

    emotion = sentiment_result["emotion"]

    confidence = sentiment_result["confidence"]

    # --------------------------------------

    history = get_history()

    response = generate_response(

        user_message,

        sentiment,

        emotion,

        history

    )

    # --------------------------------------

    add_to_memory(

        user_message,

        response

    )

    # --------------------------------------

    update_analytics(

        sentiment,

        emotion

    )

    # --------------------------------------

    return {

        "response": response,

        "sentiment": sentiment,

        "emotion": emotion,

        "confidence": confidence,

        "emoji": sentiment_result["emoji"],

        "emotion_emoji": sentiment_result["emotion_emoji"],

        "quality": response_quality(response)

    }


# ==========================================
# Get Analytics
# ==========================================

def get_analytics():

    return analytics


# ==========================================
# Get Conversation History
# ==========================================

def conversation_history():

    return get_history_list()


# ==========================================
# Reset Chat
# ==========================================

def reset_chat():

    clear_memory()

    for key in analytics.keys():

        analytics[key] = 0


# ==========================================
# Statistics
# ==========================================

def statistics():

    total = get_total_messages()

    return {

        "messages": total,

        "analytics": analytics

    }


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    print("=" * 60)

    print("Emotion-Aware Customer Support Chatbot")

    print("=" * 60)

    while True:

        message = input("\nCustomer: ")

        if message.lower() == "exit":
            break

        result = chat(message)

        print("\nAssistant:\n")

        print(result["response"])

        print("\nSentiment :", result["sentiment"])

        print("Emotion   :", result["emotion"])

        print("Confidence:", result["confidence"])

        print("Quality   :", result["quality"])

        print("-" * 60)