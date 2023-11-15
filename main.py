import openai

from agent.agent import start_conversation
from buyer_and_seller.buyer_and_seller import bas_sbp, bas_evaluator

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

# step-back-prompting
# optionale tags reserchieren (z.B.: seed)
# zwei extremen gegeneinander laufen lassen

bas_evaluator()
