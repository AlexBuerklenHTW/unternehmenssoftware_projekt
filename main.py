import openai

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()


## Simple conversation. Topic: Paul wants to sell his Iphone and Sarah is a potential buyer.
def buyer_and_seller_1():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "Paul and Sarah are going to have a conversation, that needs to end up with a deal."},
            {"role": "assistant",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "assistant",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])

##response:
# Paul: Hi Sarah, I heard you're interested in buying the used Iphone 13 I have for sale.
#
# Sarah: Hi Paul, yes, I'm definitely interested in purchasing the Iphone 13. However, I have a budget of 600€. Is there any possibility of negotiating the price?
#
# Paul: I understand your budget, but I was initially looking to sell it for 700€. However, I am willing to negotiate. How about meeting in the middle at 650€?
#
# Sarah: I appreciate your willingness to negotiate, Paul. However, my budget is quite firm at 600€. Would you consider selling it to me for that price?
#
# Paul: I understand your budget limitations, Sarah. Let's find a middle ground. How about 625€? That way, we both compromise a bit.
#
# Sarah: I appreciate your effort to meet halfway, Paul. However, I'm afraid my maximum budget is still 600€. Is there any way you could consider selling it for that price?
#
# Paul: Alright, Sarah. I can see that you really want the Iphone 13, and I'm willing to work with you on this. Since you seem really interested, I can agree to sell it to you for 600€.
#
# Sarah: Thank you, Paul! I'm glad we were able to come to an agreement. I accept your offer of 600€ for the Iphone 13.
#
# Paul: Fantastic, Sarah! I'm glad we were able to reach a deal. The Iphone 13 is now yours for 600€. I'll make sure it's properly packaged for you.
#
# Sarah: Great! I appreciate your cooperation, Paul. Can we arrange a convenient time and place for the transaction?
#
# Paul: Absolutely, Sarah. Let's organize a time and place that works for both of us. Shall we meet tomorrow afternoon at the local coffee shop at 4 pm?
#
# Sarah: That sounds perfect, Paul. I'll see you at the coffee shop tomorrow at 4 pm. Looking forward to completing the transaction.
#
# Paul: Excellent, Sarah. I'll be there, ready to hand over the Iphone 13 to you at 4 pm. See you then!
#
# Sarah: Thank you, Paul. See you tomorrow!

def buyer_and_seller_2():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "Paul and Sarah are going to have a conversation, that needs to end up with a deal."},
            {"role": "assistant",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "assistant",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])
