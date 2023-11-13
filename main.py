import openai

import buyer_and_seller.buyer_and_seller

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

## Project description:
# Provide initial description of agent (possibly hobbies, interests, CV, goals, etc.)
# For each member, decide to have conversation (on a daily basis)
# Feed conversation into memory stream
# Generate summary and feed into memory stream
# Rate each entry how interesting it was
# Generate higher-level reflections per chat partner and across chat partners
# Retrieve relevant content for conversations (history for particular member, higher-level reflections from other conversations, etc.)
# Allow user feedback/input
# Goal could be to generate as deep conversations as possible (evaluation via LLM)

# step-back-prompting
# beispiele geben für skalen
# optionale tags reserchieren (z.B.: seed)
# zwei extremen gegeneinander laufen lassen

bas = buyer_and_seller.buyer_and_seller.bas_evaluator()
