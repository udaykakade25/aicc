# Simple Chatbot using Dictionary and While Loop

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hey! Nice to meet you!",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm ChatBot, your virtual assistant!",
    "what can you do": "I can answer simple questions and have a basic conversation with you!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later! Take care!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "help": "You can ask me: hello, how are you, what is your name, what can you do, or say bye to exit.",
}

print("ChatBot: Hello! I'm ChatBot. Type 'help' to see what I can do, or 'bye' to exit.")
print("-" * 50)

while True:
    user_input = input("You: ").strip().lower()

    if not user_input:
        print("ChatBot: Please type something!")
        continue

    if user_input in ["bye", "goodbye"]:
        print(f"ChatBot: {responses[user_input]}")
        break

    if user_input in responses:
        print(f"ChatBot: {responses[user_input]}")
    else:
        print("ChatBot: I'm not sure how to respond to that. Type 'help' to see what I understand.")