"""
==========================================================
Analytics Module
Emotion-Aware Customer Support Chatbot
==========================================================
"""

import pandas as pd
import plotly.express as px


# -------------------------------------------------------
# Sentiment Pie Chart
# -------------------------------------------------------

def sentiment_chart(analytics):

    data = {
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Count": [
            analytics.get("Positive", 0),
            analytics.get("Neutral", 0),
            analytics.get("Negative", 0)
        ]
    }

    df = pd.DataFrame(data)

    fig = px.pie(
        df,
        names="Sentiment",
        values="Count",
        title="Sentiment Distribution"
    )

    return fig


# -------------------------------------------------------
# Emotion Bar Chart
# -------------------------------------------------------

def emotion_chart(analytics):

    emotions = [
        "Joy",
        "Anger",
        "Sadness",
        "Fear",
        "Surprise",
        "NeutralEmotion"
    ]

    counts = []

    for emotion in emotions:
        counts.append(analytics.get(emotion, 0))

    df = pd.DataFrame({
        "Emotion": emotions,
        "Count": counts
    })

    fig = px.bar(
        df,
        x="Emotion",
        y="Count",
        title="Emotion Distribution"
    )

    return fig


# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------

def summary_metrics(analytics):

    total_messages = (
        analytics.get("Positive", 0)
        + analytics.get("Neutral", 0)
        + analytics.get("Negative", 0)
    )

    positive = analytics.get("Positive", 0)

    neutral = analytics.get("Neutral", 0)

    negative = analytics.get("Negative", 0)

    if total_messages == 0:

        return {

            "Total Messages": 0,

            "Positive %": 0,

            "Neutral %": 0,

            "Negative %": 0

        }

    return {

        "Total Messages": total_messages,

        "Positive %": round(
            positive / total_messages * 100,
            2
        ),

        "Neutral %": round(
            neutral / total_messages * 100,
            2
        ),

        "Negative %": round(
            negative / total_messages * 100,
            2
        )

    }


# -------------------------------------------------------
# Emotion Statistics
# -------------------------------------------------------

def emotion_statistics(analytics):

    emotions = [

        "Joy",

        "Anger",

        "Sadness",

        "Fear",

        "Surprise",

        "NeutralEmotion"

    ]

    stats = {}

    for emotion in emotions:

        stats[emotion] = analytics.get(emotion, 0)

    return stats


# -------------------------------------------------------
# Most Frequent Emotion
# -------------------------------------------------------

def dominant_emotion(analytics):

    emotions = {

        "Joy": analytics.get("Joy", 0),

        "Anger": analytics.get("Anger", 0),

        "Sadness": analytics.get("Sadness", 0),

        "Fear": analytics.get("Fear", 0),

        "Surprise": analytics.get("Surprise", 0),

        "NeutralEmotion": analytics.get("NeutralEmotion", 0)

    }

    return max(

        emotions,

        key=emotions.get

    )


# -------------------------------------------------------
# Export Analytics
# -------------------------------------------------------

def analytics_dataframe(analytics):

    df = pd.DataFrame({

        "Category": analytics.keys(),

        "Count": analytics.values()

    })

    return df


# -------------------------------------------------------
# Testing
# -------------------------------------------------------

if __name__ == "__main__":

    sample = {

        "Positive": 18,

        "Neutral": 12,

        "Negative": 8,

        "Joy": 14,

        "Anger": 5,

        "Sadness": 3,

        "Fear": 2,

        "Surprise": 4,

        "NeutralEmotion": 10

    }

    print(summary_metrics(sample))

    print(emotion_statistics(sample))

    print(dominant_emotion(sample))