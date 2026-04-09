def response(user_input):
    text = user_input.lower().strip()
    if text == "hello" or text == "hi" or text == "hey":
        return "Hello! How can I be of assistance?"
    elif text == "how are you?" or text == "how are you today?":
        return "I'm doing well,thank you! How are you?"
    elif text == "bye" or text == "exit" or text == "goodbye":
        return "Goodbye! It was nice talking and being of assistance today! Have a lovely day!"
    elif text == "what is:" or text == "what does AIU offer?" or text == "what does AIU charge per semester?":
        return "AIU offers a variety of programs in fields such as Technology, Theology, Business, and Teaching"
    elif text == "help":
        return "I can help you with all the information you need about AIU."
def main():
    print("Welcome to the AIU Information Bot! Type 'help' for assistance or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "bye", "goodbye"]:
            print("PyBot: Goodbye! Thanks for enquiring about AIU.You can always come back anytime.Have a great day!")
            break
        response_text = response(user_input)
        print(f"PyBot: {response_text}\n")
        if not user_input:
            continue
if __name__ == "__main__":
    main()
    
    
    