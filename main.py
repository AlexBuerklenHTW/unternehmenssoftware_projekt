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

# chat_agent_seller = [{"role": "system", "content": "You are a seller of a phone. The price of the phone is 800€."}]
# chat_agent_buyer = [{"role": "system", "content": "You are a buyer of a phone. You want to buy it for 600€"}]
# chat_response_seller = [{"role": "assistant", "content": ""}]
# chat_response_buyer = [{"role": "assistant", "content": ""}]
#
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "system", "content": "You are a seller of a phone. The price of the phone is 800€."}]
# )
# final_response = response['choices'][0]['message']['content']
# print("ChatGPT:", final_response.strip())


# Define the conversation where the user provides a topic, and both assistants discuss it back and forth five times
conversation = [
    {"role": "user", "content": "Let's discuss the impact of artificial intelligence on society."}
]

# Function to send a message to the API
def send_message(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Number of back-and-forth exchanges
num_exchanges = 5

for _ in range(num_exchanges):
    # Assistant 1 responds
    assistant1_response = send_message(conversation + [{"role": "assistant", "content": "Assistant 1, what are your thoughts on the topic?"}])
    conversation.append({"role": "assistant", "content": assistant1_response})

    # Assistant 2 responds
    assistant2_response = send_message(conversation + [{"role": "assistant", "content": "Assistant 2, please share your insights as well."}])
    conversation.append({"role": "assistant", "content": assistant2_response})

    # Print the conversation
    print("User:", conversation[0]["content"])
    for i in range(1, len(conversation), 2):
        print(f"Assistant 1: {conversation[i]['content']}")
        print(f"Assistant 2: {conversation[i + 1]['content']}\n")


