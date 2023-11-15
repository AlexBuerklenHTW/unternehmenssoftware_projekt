import openai


file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()


def agent_java_and_python():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a Java expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Java is the best language"
                        "and that you can solve any problem with Java."},
            {"role": "system",
             "content": "You are a Python expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Python is the best language"
                        "and that you can solve any problem with Python."}
        ]
    )
    return response['choices'][0]['message']['content']


def start_conversation():

    starter = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "We need to build a E-Commerce platform, where we sell computer hardware. What programming language should we use for backend? Java or python?"},
            {"role": "assistant",
             "content": agent_java()},
            {"role": "assistant",
             "content": agent_python()}
        ]
    )

    print(starter['choices'][0]['message']['content'])

