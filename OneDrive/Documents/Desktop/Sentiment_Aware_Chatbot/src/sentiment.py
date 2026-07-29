from transformers import pipeline

# -------------------------------------------------
# Sentiment Model
# -------------------------------------------------

sentiment_pipeline = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    top_k=None
)

# -------------------------------------------------
# Emotion Keywords
# -------------------------------------------------

EMOTION_KEYWORDS = {
    "Joy": [
        "happy", "great", "excellent", "awesome",
        "love", "fantastic", "good", "wonderful",
        "thanks", "thank you", "amazing"
    ],

    "Anger": [
        "angry", "furious", "hate", "terrible",
        "worst", "useless", "annoyed",
        "frustrated", "disappointed"
    ],

    "Sadness": [
        "sad", "cry", "upset", "depressed",
        "heartbroken", "unhappy", "lonely"
    ],

    "Fear": [
        "worried", "afraid", "fear",
        "scared", "panic", "anxious"
    ],

    "Surprise": [
        "wow", "unexpected", "surprised",
        "unbelievable", "really"
    ]
}

# -------------------------------------------------
# Emoji Mapping
# -------------------------------------------------

EMOJI = {
    "Positive": "😊",
    "Neutral": "😐",
    "Negative": "😞",

    "Joy": "😁",
    "Anger": "😡",
    "Sadness": "😢",
    "Fear": "😨",
    "Surprise": "😲",
    "NeutralEmotion": "😐"
}


# -------------------------------------------------
# Detect Emotion
# -------------------------------------------------

def detect_emotion(text):

    text = text.lower()

    scores = {}

    for emotion, words in EMOTION_KEYWORDS.items():

        count = 0

        for word in words:

            if word in text:
                count += 1

        scores[emotion] = count

    if max(scores.values()) == 0:
        return "NeutralEmotion"

    return max(scores, key=scores.get)


# -------------------------------------------------
# Detect Sentiment
# -------------------------------------------------

def detect_sentiment(text):

    result = sentiment_pipeline(text)[0]

    best = max(result, key=lambda x: x["score"])

    label = best["label"]

    confidence = round(best["score"] * 100, 2)

    emotion = detect_emotion(text)

    return {

        "sentiment": label,

        "confidence": confidence,

        "emotion": emotion,

        "emoji": EMOJI.get(label, "🙂"),

        "emotion_emoji": EMOJI.get(emotion, "🙂")
    }


# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":

    while True:

        text = input("Message: ")

        output = detect_sentiment(text)

        print(output)