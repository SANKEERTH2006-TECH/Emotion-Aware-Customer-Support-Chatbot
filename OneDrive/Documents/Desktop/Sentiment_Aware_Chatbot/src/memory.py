# ==========================================
# Conversation Memory Manager
# ==========================================

MAX_HISTORY = 10

conversation_history = []


def add_to_memory(user_message, assistant_response):
    """
    Save one conversation turn.
    """

    global conversation_history

    conversation_history.append({
        "user": user_message,
        "assistant": assistant_response
    })

    # Keep only the most recent conversations
    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]


def get_history():
    """
    Return conversation history as formatted text.
    """

    if not conversation_history:
        return ""

    history = ""

    for chat in conversation_history:

        history += (
            f"User: {chat['user']}\n"
            f"Assistant: {chat['assistant']}\n\n"
        )

    return history.strip()


def clear_memory():
    """
    Clear all stored conversations.
    """

    global conversation_history
    conversation_history = []


def get_history_list():
    """
    Return conversation history as a list.
    """

    return conversation_history


def get_total_messages():
    """
    Total conversation turns.
    """

    return len(conversation_history)


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    add_to_memory(
        "Hi",
        "Hello! How can I help you?"
    )

    add_to_memory(
        "My internet is not working.",
        "I'm sorry to hear that. Let's troubleshoot it together."
    )

    print(get_history())

    print("\nTotal Messages:", get_total_messages())