# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day."
    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that."

print("Welcome to ChatBot! (type 'bye' to exit)")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
        break
