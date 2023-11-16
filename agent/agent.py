import openai

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()


def agent_java_and_python_names():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant",
             "content": "You take the role of a Java expert (Paul). You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Java is the best language"
                        "and that you can solve any problem with Java."
                        "You work for Company X. Company X wants to decide between java and python for backend. You are going to "
                        "defend Java in the discussion."},
            {"role": "assistant",
             "content": "You take the role of a Python expert (Sarah). You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Python is the best language"
                        "and that you can solve any problem with Python."
                        "You work for Company X. Company X wants to decide between java and python for backend. You are going to "
                        "defend Python in the discussion."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def agent_java_and_python_no_names():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant",
             "content": "You take the role of a Java expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Java is the best language"
                        "and that you can solve any problem with Java."
                        "You work for Company X. Company X wants to decide between java and python for backend. You are going to "
                        "defend Java in the discussion."},
            {"role": "assistant",
             "content": "You take the role of a Python expert. You learned this programming language since you started learning programming."
                        "You worked in a lot of companies and on a lot of projects. You think, Python is the best language"
                        "and that you can solve any problem with Python."
                        "You work for Company X. Company X wants to decide between java and python for backend. You are going to "
                        "defend Python in the discussion."}
        ]
    )
    print(response['choices'][0]['message']['content'])
