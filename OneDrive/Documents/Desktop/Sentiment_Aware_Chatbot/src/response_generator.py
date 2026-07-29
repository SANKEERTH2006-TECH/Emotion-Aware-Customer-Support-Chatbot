from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

print("Loading FLAN-T5 model...")

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("FLAN-T5 Loaded Successfully!")

# ---------------------------------------------------
# Prompt Builder
# ---------------------------------------------------

def build_prompt(user_message, sentiment, emotion, history=""):

    style = {
        "Positive":
            "Respond in a warm, cheerful, encouraging, and professional manner.",

        "Neutral":
            "Respond politely and professionally.",

        "Negative":
            "Respond empathetically. Acknowledge the customer's frustration and provide reassurance."
    }

    emotion_style = {

        "Joy":
            "Celebrate the customer's positive experience.",

        "Anger":
            "Stay calm, apologize sincerely, and focus on solving the issue.",

        "Sadness":
            "Show empathy, compassion, and encouragement.",

        "Fear":
            "Provide reassurance and explain things clearly.",

        "Surprise":
            "Acknowledge the unexpected situation and provide clarification.",

        "NeutralEmotion":
            "Provide a clear and informative response."
    }

    prompt = f"""
You are an expert AI Customer Support Assistant.

Your goals are:

1. Understand the customer's emotion.
2. Reply professionally.
3. Be empathetic.
4. Keep responses concise.
5. Offer practical help.

Conversation History:
{history}

Detected Sentiment:
{sentiment}

Detected Emotion:
{emotion}

Customer Message:
{user_message}

Instructions:

{style.get(sentiment)}

{emotion_style.get(emotion)}

Generate only the assistant's response.
"""

    return prompt


# ---------------------------------------------------
# Generate Response
# ---------------------------------------------------

def generate_response(user_message,
                      sentiment,
                      emotion,
                      history=""):

    prompt = build_prompt(
        user_message,
        sentiment,
        emotion,
        history
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.6,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.15
        )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response.strip()


# ---------------------------------------------------
# Testing
# ---------------------------------------------------

if __name__ == "__main__":

    while True:

        text = input("Customer: ")

        response = generate_response(
            text,
            "Negative",
            "Anger"
        )

        print("\nAssistant:\n")
        print(response)
        print("-" * 60)