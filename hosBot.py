def response(user_input):    
    text = user_input.lower().strip()    
    if text == "hello" or text == "hey":
      return "Hello! How can I help?"
    elif text == "headache" or text == "fever":
       return "Noted. How long? Any other symptoms?"
    elif text == "i have had the symptoms for 2 days":
       return "Noted. Two days with the symptoms you need to visit a hospital"
    elif text == "what should i do?":
       return "Based on MOH guidelines, you may need to stay hydrated,rest and visit a health facility"
    elif text == "help":
       return "How do you need me to help.I can help with finding the nearest open facility"
    elif text == "help me":
       return "I can help you with all health information"
    elif text == "thank you":
       return "Always happy to help!"
    elif text == "exit" or text =="bye":
       return "Have a good day and thanks for trusting me!"
    else:
       return "Sorry, I didn't catch that. Type 'help' for options."
def main():
   print("Welcome to the MOH information Bot! Type 'help' for assistance or 'exit' to quit")
   while True:
      user_input = input("User: ").strip()
      if not user_input:
            continue
      if user_input.lower() in ["exit", "bye"]:
         print("HosBot: Have a good day and thanks for trusting me!")
         break
      response_text = response(user_input)
      print("HosBot:", response_text)
if __name__ == "__main__":
   main()

    