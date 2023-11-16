import openai

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

# step-back-prompting
