import streamlit as st
st.write("🚀 TASK 5 APP IS RUNNING")

from src.chatbot import (
    chat,
    get_analytics,
    conversation_history,
    reset_chat
)

from src.analytics import (
    sentiment_chart,
    emotion_chart,
    summary_metrics,
    dominant_emotion
)

# ---------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Emotion-Aware Customer Support Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🤖 Emotion-Aware Chatbot")

    st.markdown("---")

    st.write("### Features")

    st.success("✅ Sentiment Detection")
    st.success("✅ Emotion Detection")
    st.success("✅ Conversation Memory")
    st.success("✅ AI Response Generation")
    st.success("✅ Analytics Dashboard")

    st.markdown("---")

    if st.button("🗑 Clear Conversation"):

        reset_chat()

        st.session_state.chat_messages = []

        st.success("Conversation Cleared")

    st.markdown("---")

    st.info(
        """
This chatbot detects customer emotions
and generates empathetic responses using
an Open Source Large Language Model.
"""
    )

# ---------------------------------------------------
# Main Title
# ---------------------------------------------------

st.title("🤖 Emotion-Aware Customer Support Chatbot")

st.write(
"""
Analyze customer emotions and generate
empathetic AI-powered responses.
"""
)

st.markdown("---")

# ---------------------------------------------------
# Layout
# ---------------------------------------------------

left, right = st.columns([2, 1])

with left:

    user_input = st.text_area(
        "Customer Message",
        height=140,
        placeholder="Type your message here..."
    )

    send = st.button(
        "Send Message",
        use_container_width=True
    )

with right:

    st.subheader("Project")

    st.write("Task 5")

    st.write("Emotion-Aware Customer Support")

    st.write("Open Source LLM")

    st.write("Streamlit")

st.markdown("---")

# ---------------------------------------------------
# Chat Processing
# ---------------------------------------------------

if send:

    if user_input.strip() == "":

        st.warning("Please enter a customer message.")

    else:

        with st.spinner("Analyzing customer sentiment..."):

            result = chat(user_input)

        st.session_state.chat_messages.append({

            "user": user_input,

            "assistant": result["response"],

            "sentiment": result["sentiment"],

            "emotion": result["emotion"],

            "confidence": result["confidence"],

            "emoji": result["emoji"],

            "emotion_emoji": result["emotion_emoji"],

            "quality": result["quality"]

        })

# ---------------------------------------------------
# Chat History
# ---------------------------------------------------

if len(st.session_state.chat_messages) > 0:

    st.header("💬 Conversation")

    for message in reversed(st.session_state.chat_messages):

        # ---------------- USER ----------------

        with st.chat_message("user"):

            st.write(message["user"])

        # ---------------- BOT -----------------

        with st.chat_message("assistant"):

            st.write(message["assistant"])

            col1, col2 = st.columns(2)

            with col1:

                st.metric(

                    "Sentiment",

                    f"{message['emoji']} {message['sentiment']}"

                )

                st.metric(

                    "Emotion",

                    f"{message['emotion_emoji']} {message['emotion']}"

                )

            with col2:

                st.metric(

                    "Confidence",

                    f"{message['confidence']:.2f}%"

                )

                st.metric(

                    "Response Quality",

                    message["quality"]

                )

        st.markdown("---")

else:

    st.info("Start a conversation to see responses.")

    # ---------------------------------------------------
# Analytics Dashboard
# ---------------------------------------------------

st.markdown("---")

analytics = get_analytics()

summary = summary_metrics(analytics)

st.header("📊 Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Messages",
        summary["Total Messages"]
    )

with col2:
    st.metric(
        "Positive %",
        f'{summary["Positive %"]}%'
    )

with col3:
    st.metric(
        "Neutral %",
        f'{summary["Neutral %"]}%'
    )

with col4:
    st.metric(
        "Negative %",
        f'{summary["Negative %"]}%'
    )

st.markdown("---")

chart1, chart2 = st.columns(2)

with chart1:

    st.plotly_chart(

        sentiment_chart(analytics),

        use_container_width=True

    )

with chart2:

    st.plotly_chart(

        emotion_chart(analytics),

        use_container_width=True

    )

st.markdown("---")

st.subheader("🎯 Dominant Customer Emotion")

st.success(dominant_emotion(analytics))

# ---------------------------------------------------
# Conversation History
# ---------------------------------------------------

st.markdown("---")

st.header("📜 Conversation History")

history = conversation_history()

if len(history) == 0:

    st.info("No conversations yet.")

else:

    for index, item in enumerate(history, start=1):

        with st.expander(f"Conversation {index}"):

            st.write("### 👤 Customer")

            st.write(item["user"])

            st.write("### 🤖 Assistant")

            st.write(item["assistant"])

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.caption(
    """
Emotion-Aware Customer Support Chatbot

Built using

• Streamlit

• Transformers

• RoBERTa

• FLAN-T5

• Plotly

• Scikit-Learn

This chatbot is intended for educational and internship purposes.
"""
)