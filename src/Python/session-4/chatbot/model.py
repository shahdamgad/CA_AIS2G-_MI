import random
import json

# to read file with open and 'r' is to read and is called as file
with open("data.json", "r") as file:
    responses = json.load(file)

def get_response(user_input: str) -> str:
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])