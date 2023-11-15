import openai


## Topic (buyer and seller): Paul wants to sell his Iphone and Sarah is a potential buyer.
# bas = buyer and seller
# sbp = step back prompting

def bas_assistant():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "assistant",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def bas_user():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "user",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def bas_system():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "system",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def bas_sbp():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Paul is a professional seller and Sarah is a professional seller. They both use professional strategies for negotiation"},
            {"role": "assistant",
             "content": "You take the role of a seller (name: Paul). You have a used Iphone 13, that you want to sell for 700€. You are ready to negotiate, but not under 500€."},
            {"role": "assistant",
             "content": "You take the role of a buyer (name: Sarah). You are interested in the Iphone 13. You have a budget of 600€. You want to negotiate down to 550€, but would take the Iphone 13 for 600€."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def bas_evaluator():
    first_run_bas = """1st run:"
                 "Paul: Hi Sarah, I heard you're interested in buying the used Iphone 13 I have for sale."
                 "Sarah: Hi Paul, yes, I'm definitely interested in purchasing the Iphone 13. However, I have a budget of 600€. Is there any possibility of negotiating the price?"
                 "Paul: I understand your budget, but I was initially looking to sell it for 700€. However, I am willing to negotiate. How about meeting in the middle at 650€?"
                 "Sarah: I appreciate your willingness to negotiate, Paul. However, my budget is quite firm at 600€. Would you consider selling it to me for that price?"
                 "Paul: I understand your budget limitations, Sarah. Let's find a middle ground. How about 625€? That way, we both compromise a bit."
                 "Sarah: I appreciate your effort to meet halfway, Paul. However, I'm afraid my maximum budget is still 600€. Is there any way you could consider selling it for that price?"
                 "Paul: Alright, Sarah. I can see that you really want the Iphone 13, and I'm willing to work with you on this. Since you seem really interested, I can agree to sell it to you for 600€."
                 "Sarah: Thank you, Paul! I'm glad we were able to come to an agreement. I accept your offer of 600€ for the Iphone 13."
                 "Paul: Fantastic, Sarah! I'm glad we were able to reach a deal. The Iphone 13 is now yours for 600€. I'll make sure it's properly packaged for you."
                 "Sarah: Great! I appreciate your cooperation, Paul. Can we arrange a convenient time and place for the transaction?"
                 "Paul: Absolutely, Sarah. Let's organize a time and place that works for both of us. Shall we meet tomorrow afternoon at the local coffee shop at 4 pm?"
                 "Sarah: That sounds perfect, Paul. I'll see you at the coffee shop tomorrow at 4 pm. Looking forward to completing the transaction."
                 "Paul: Excellent, Sarah. I'll be there, ready to hand over the Iphone 13 to you at 4 pm. See you then!"
                 "Sarah: Thank you, Paul. See you tomorrow!"""
    second_run_bas = """2nd run:"
                  "Paul: Hi Sarah, I heard you're looking for an Iphone 13. I happen to have a used one that I'm looking to sell. Are you interested?"
                  "Sarah: Yes, I am. I've been searching for a good deal on an Iphone 13. How much are you asking for it?"
                  "Paul: I'm looking to sell it for 700€. It's in great condition and still functions perfectly. However, I am open to negotiations. What's your budget?"
                  "Sarah: My budget is around 600€. I understand that it's a used phone, so I believe that price is fair. Would you consider selling it for 600€?"
                  "Paul: I appreciate your offer, Sarah. I understand your budget concerns, but I'm afraid 600€ is a bit too low for me. I have taken good care of the phone, and it still holds its value. Would you be able to increase your offer?"
                  "Sarah: I understand your point, Paul. Can we meet halfway at 550€? I think that would be a fair compromise considering it's a used phone."
                  "Paul: Thank you for the compromise, Sarah. I do believe the phone is worth more, but I am willing to meet you halfway. If you can agree to 575€, then we have a deal."
                  "Sarah: 575€ is a bit higher than my initial budget, but I think I can make that work. I appreciate your flexibility, Paul. Let's make it a deal."
                  "Paul: Great! I'm glad we were able to reach an agreement. The Iphone 13 is yours for 575€. I'll make sure to prepare it for you and we can arrange a time for the exchange."""
    third_run_bas = """3rd run:"
                 "Paul: Hi Sarah! I heard you're interested in purchasing an iPhone 13. I have a used one available for sale. How can I assist you?"
                 "Sarah: Hi Paul! Yes, I've been looking for an iPhone 13 at a reasonable price. Can you tell me more about the condition of the phone and the price you're asking for it?"
                 "Paul: Certainly! The iPhone 13 I have is in great condition, with no major scratches or dents. It has been well-maintained and functions perfectly. As for the price, I'm looking to sell it for 700€. However, I am open to negotiation."
                 "Sarah: That sounds promising, Paul. I understand that you're willing to negotiate. Considering my budget, would you consider selling it for 550€?"
                 "Paul: I appreciate your offer, Sarah. While I understand your budget, I can't go as low as 550€. However, I could meet you halfway at 650€. What do you think?"
                 "Sarah: Hmm, that's still a bit more than I was hoping to spend. Is there any chance you could consider selling it for 600€?"
                 "Paul: I understand your budget concerns, Sarah. Let's see if we can reach a compromise. How about we settle at 625€? It would be a discount for you, and I believe it's a fair middle ground."
                 "Sarah: That's closer to my budget, Paul, but can we push it just a bit further to 600€? I assure you, it's the most I can afford."
                 "Paul: I appreciate your commitment, Sarah. Given your dedication and enthusiasm, I can agree to sell the iPhone 13 to you for 600€, which is slightly below my desired price. Let's make a deal!"
                 "Sarah: Thank you so much, Paul! I'm really excited to get my hands on the iPhone 13. Let's finalize the transaction."
                 "Paul: Fantastic! I'm glad we were able to come to an agreement. We can arrange the payment and delivery details to suit both our convenience. Thank you for your cooperation, Sarah!"
                 "Sarah: Likewise, Paul! I'm looking forward to completing this transaction smoothly. Thank you for your understanding and flexibility."""
    fourth_run_bas_sbp = """4th run:"
                          "Paul: Hello Sarah, I see that you're interested in the iPhone 13. It's a great device and I'm sure you'll be satisfied with it. I have it listed for 700€, but I'm open to negotiation. Can I ask what makes you interested in this particular iPhone?"
                          "Sarah: Hi Paul, thank you for getting in touch. I've been in the market for an iPhone 13 for a while now, and your listing caught my attention. I've done my research, and I know it's a top-of-the-line device with impressive features. However, my budget is 600€. I'm willing to negotiate with you to reach a fair price.) "
                          "Paul: I appreciate your interest, Sarah. I understand your budget constraints, but I'm unable to go as low as 550€. The minimum price I can offer is 650€. This is already a significant reduction from the original listing price. Can you consider this offer?"
                          "Sarah: Thank you for considering my budget, Paul. I understand that you're offering a reduced price, but 650€ is still a bit over my limit. I can stretch my budget to 600€, and that's the most I can offer. "
                          "Paul: I understand that you have a budget, Sarah, but considering the current market value of the iPhone 13 and its features, I believe 600€ is still a bit lower than what it's worth. However, I can meet you halfway at 625€. This way, we both compromise and reach a fair agreement. "
                          "Sarah: I appreciate your willingness to negotiate, Paul. However, 625€ is still slightly higher than I'm comfortable paying. I understand the value of the iPhone 13, but I've also seen similar devices listed for around 600€ in other places. Can you consider coming down to 600€?"
                          "Paul: I can see that you've done your research, Sarah. Considering the market prices you mentioned, I can agree to sell you the iPhone 13 for 600€. Although it's a bit lower than my initial asking price, I believe it's a fair compromise. "
                          "Sarah: That sounds great, Paul. Thank you for agreeing to my offer. I'm satisfied with the price, and I'm looking forward to owning the iPhone 13. How should we proceed with the payment and shipping details?"
                          "Paul: I'm glad we could reach a mutual agreement, Sarah. We can proceed with the payment through a secure online platform. I'll provide you with the necessary details and ensure that the shipping is handled promptly. Is there a preferred shipping method or any special instructions you have?"
                          "Sarah: That sounds good, Paul. I prefer a tracked shipping method to ensure the safety of the item during transit. Other than that, I don't have any specific instructions. I'll wait for your message with the payment details so that we can finalize the transaction. Thank you again!"
                          "Paul: Absolutely, Sarah. I'll make sure to arrange a tracked shipping method for you. I'll send you the payment details shortly, and we can proceed from there. Thank you for choosing to purchase the iPhone 13 from me, and I'm confident you'll be satisfied with your new device."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are gonna be the evaluator of responses generated by yourself. The topic is: Paul and Sarah are going to have a conversation, that needs to end up with a deal."
                        "The scale starts from 1 being a bad deal for the seller and a good deal for the buyer to 10 being a bad deal for the buyer and a good deal for the seller."
                        "Example: 1 could be if the seller goes under his pain limit and sells under his limit and the buyer bought under his target goal of the budget. 10 could be if the buyer bought over the"
                        "budget limit and the seller sold for the target price."},
            {"role": "user", "content": fourth_run_bas_sbp}
        ]
    )
    print(response['choices'][0]['message']['content'])
