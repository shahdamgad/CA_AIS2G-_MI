from model import get_response

def main_bot():
    print("chatbot: hi how i can help you?")
    while True:
        user_input = input("user: ").lower()
        response = get_response(user_input)
        print(f"chatbot: {response}")

        if user_input == "goodbye":
            break
   