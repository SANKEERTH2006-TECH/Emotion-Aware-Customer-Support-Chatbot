"""
==========================================
Utility Functions
Emotion-Aware Customer Support Chatbot
==========================================
"""

from datetime import datetime
import re


# ==========================================================
# Current Timestamp
# ==========================================================

def current_timestamp():
    """
    Returns current date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ==========================================================
# Clean Text
# ==========================================================

def clean_text(text):

    if text is None:
        return ""

    text = text.strip()

    text = re.sub(r"\s+", " ", text)

    return text


# ==========================================================
# Format Confidence
# ==========================================================

def format_confidence(score):

    return f"{score:.2f}%"


# ==========================================================
# Sentiment Color
# ==========================================================

def sentiment_color(sentiment):

    colors = {

        "Positive": "green",

        "Neutral": "orange",

        "Negative": "red"

    }

    return colors.get(sentiment, "gray")


# ==========================================================
# Emoji Mapping
# ==========================================================

def sentiment_emoji(sentiment):

    emojis = {

        "Positive": "😊",

        "Neutral": "😐",

        "Negative": "😞"

    }

    return emojis.get(sentiment, "🙂")


# ==========================================================
# Emotion Emoji
# ==========================================================

def emotion_emoji(emotion):

    emojis = {

        "Joy": "😁",

        "Anger": "😡",

        "Sadness": "😢",

        "Fear": "😨",

        "Surprise": "😲",

        "NeutralEmotion": "😐"

    }

    return emojis.get(emotion, "🙂")


# ==========================================================
# Format Conversation
# ==========================================================

def format_message(role, message):

    timestamp = current_timestamp()

    return {

        "role": role,

        "message": message,

        "timestamp": timestamp

    }


# ==========================================================
# Display Conversation
# ==========================================================

def history_to_text(history):

    if len(history) == 0:
        return "No conversation yet."

    text = ""

    for item in history:

        text += f"{item['timestamp']}\n"

        text += f"{item['role']}:\n"

        text += f"{item['message']}\n"

        text += "-" * 50 + "\n"

    return text


# ==========================================================
# Response Length
# ==========================================================

def response_length(response):

    return len(response.split())


# ==========================================================
# Simple Quality Score
# ==========================================================

def response_quality(response):

    words = response_length(response)

    if words < 8:

        return "Low"

    elif words < 25:

        return "Medium"

    return "High"


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    print(current_timestamp())

    print(format_confidence(98.4567))

    print(sentiment_color("Positive"))

    print(sentiment_emoji("Negative"))

    print(emotion_emoji("Joy"))

    print(response_quality(
        "I'm sorry to hear that. Let me help you solve the issue."
    ))