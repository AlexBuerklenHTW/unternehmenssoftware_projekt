import openai


def agent_java(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a Java expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Java is the best language"
                        "and that you can solve any problem with Java."},
            {"role": "assistant",
             "content": "You are ready to defend Java in an argument as best as you can"},
            {"role": "user",
             "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']


def agent_python(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a Python expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Python is the best language"
                        "and that you can solve any problem with Python."},
            {"role": "assistant",
             "content": "You are ready to defend Python in an argument as best as you can"},
            {"role": "user",
             "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']


def starter():
    user_input = "What would be more suitable in the backend for developing an E-Commerce Platform? Java or Python?"
    return user_input


def conversation():
    user_prompt = starter()

    for _ in range(3):  # You can adjust the number of turns in the conversation
        java_response = agent_java(user_prompt)
        print(f"Java Expert: {java_response}")

        python_response = agent_python(java_response)
        print(f"Python Expert: {python_response}")

        user_prompt = python_response  # Set the user prompt to the last agent's response


conversation()
