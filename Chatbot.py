def chatbot():
    print("Bot: Hi! Type 'bye' anytime to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I am fine ,thanks!")

        elif user == "bye":
            print("Bot:Good Bye!")
            break

        else:
             print("Bot: Sorry, I didn't get that.")


chatbot()
        

