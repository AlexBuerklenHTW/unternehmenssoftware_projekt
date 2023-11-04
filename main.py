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

chat_agent_seller = [{"role": "system", "content": "You are a seller of a phone. The price of the phone is 800€."}]
chat_agent_buyer = [{"role": "system", "content": "You are a buyer of a phone. You want to buy it for 600€"}]
chat_response_seller = [{"role": "assistant", "content": ""}]
chat_response_buyer = []

while True:

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_response_seller
    )
    assistant_response = response['choices'][0]['message']['content']
    print("ChatGPT:", assistant_response.strip())

    # Add ChatGPT's response to the conversation log
    chat_log.append({"role": "assistant", "content": assistant_response})

