import openai

from agent.agent import agent_java_and_python_names, agent_java_and_python_names_temperature

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

# step-back-prompting
# optionale tags reserchieren (z.B.: seed)
# zwei extremen gegeneinander laufen lassen

agent_java_and_python_names_temperature()
