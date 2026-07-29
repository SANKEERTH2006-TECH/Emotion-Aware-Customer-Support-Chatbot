# ============================================
# Response Validator
# ============================================

import re


MIN_RESPONSE_LENGTH = 20


# --------------------------------------------------------
# Remove Extra Spaces
# --------------------------------------------------------

def clean_response(response):

    response = response.replace("\n", " ")

    response = re.sub(r"\s+", " ", response)

    return response.strip()


# --------------------------------------------------------
# Check if Empty
# --------------------------------------------------------

def is_empty(response):

    if response is None:
        return True

    if len(response.strip()) == 0:
        return True

    return False


# --------------------------------------------------------
# Check Repeated Sentences
# --------------------------------------------------------

def has_repetition(response):

    words = response.lower().split()

    if len(words) < 6:
        return False

    unique_words = len(set(words))

    ratio = unique_words / len(words)

    if ratio < 0.45:
        return True

    return False


# --------------------------------------------------------
# Response Too Short
# --------------------------------------------------------

def too_short(response):

    return len(response) < MIN_RESPONSE_LENGTH


# --------------------------------------------------------
# Sentiment Check
# --------------------------------------------------------

def validate_sentiment(sentiment, response):

    response = response.lower()

    if sentiment == "Negative":

        keywords = [
            "sorry",
            "understand",
            "apologize",
            "help",
            "assist"
        ]

    elif sentiment == "Positive":

        keywords = [
            "great",
            "glad",
            "happy",
            "wonderful",
            "thank"
        ]

    else:

        keywords = [
            "information",
            "details",
            "explain",
            "provide"
        ]

    score = 0

    for word in keywords:

        if word in response:
            score += 1

    return score >= 1


# --------------------------------------------------------
# Fallback Responses
# --------------------------------------------------------

def fallback_response(sentiment):

    if sentiment == "Negative":

        return (
            "I'm sorry you're experiencing this issue. "
            "I understand how frustrating this can be. "
            "Please provide a little more detail so I can help you effectively."
        )

    elif sentiment == "Positive":

        return (
            "That's wonderful to hear! "
            "I'm glad everything is going well. "
            "Please let me know if there's anything else I can help you with."
        )

    return (
        "Thank you for your question. "
        "Could you please provide a little more information so I can give a more accurate answer?"
    )


# --------------------------------------------------------
# Main Validator
# --------------------------------------------------------

def validate_response(
    response,
    sentiment
):

    if is_empty(response):

        return fallback_response(sentiment)

    response = clean_response(response)

    if too_short(response):

        return fallback_response(sentiment)

    if has_repetition(response):

        return fallback_response(sentiment)

    if not validate_sentiment(sentiment, response):

        return fallback_response(sentiment)

    return response


# --------------------------------------------------------
# Testing
# --------------------------------------------------------

if __name__ == "__main__":

    sample = "Sorry. Sorry. Sorry. Sorry."

    print(validate_response(sample, "Negative"))

    sample = "I'm sorry you're facing this issue. Let me help you resolve it."

    print(validate_response(sample, "Negative"))