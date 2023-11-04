import openai

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

## Code below is basically chatGPT, but in code

# chat_log = []
#
# while True:
#     user_message = input()
#     if user_message.lower() == "quit":
#         break
#     else:
#         chat_log.append({"role": "user", "content": user_message})
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=chat_log
#         )
#         assistant_response = response['choices'][0]['message']['content']
#         print("ChatGPT:", assistant_response.strip("\n").strip())
#         chat_log.append({"role": "user", "content": assistant_response.strip("\n").strip()})

## Code below shows, that it is not possible to create a "biased" response, since OpenaAI is trying to avoid biased responses

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You only like Apple products"},
#         {"role": "user", "content": "Do you recommend apple products or samsung products?"}
#     ]
# )
# print(response)


## Code below sets a context with the role set to "system".

# chat_log = []

# Initialize the conversation with ChatGPT acting as a seller
# chat_log.append({"role": "system", "content": "You are a seller of a phone. The price of the phone is 800€."})
#
# while True:
#     user_message = input("User: ")
#     if user_message.lower() == "quit":
#         break
#
#     # User interaction
#     chat_log.append({"role": "user", "content": user_message})
#
#     # Generate a response from ChatGPT
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=chat_log
#     )
#     assistant_response = response['choices'][0]['message']['content']
#     print("ChatGPT:", assistant_response.strip())
#
#     # Add ChatGPT's response to the conversation log
#     chat_log.append({"role": "assistant", "content": assistant_response})

def assistant_1(chat_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    return response['choices'][0]['message']['content']


def assistant_2(chat_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    return response['choices'][1]['message']['content']


# Initialize the conversation with two AI "assistants"
chat_log = [
    {"role": "assistant_1", "content": "Hello, I am Assistant 1."},
    {"role": "assistant_2", "content": "Hi, I am Assistant 2."}
]

while True:
    user_message = input("User: ")
    if user_message.lower() == "quit":
        break

    # User interaction (optional)
    chat_log.append({"role": "user", "content": user_message})

    # Get responses from both assistants
    assistant_1_response = assistant_1(chat_log)
    assistant_2_response = assistant_2(chat_log)

    # Print and update the conversation log
    print("Assistant 1:", assistant_1_response.strip())
    print("Assistant 2:", assistant_2_response.strip())

    chat_log.append({"role": "assistant_1", "content": assistant_1_response})
    chat_log.append({"role": "assistant_2", "content": assistant_2_response})
