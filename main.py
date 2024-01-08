import streamlit as st
import openai
import chromadb as db

client = openai

chroma_client = db.Client()

collection = chroma_client.get_or_create_collection(name="main_collection")

file_path = "API_KEY"
client.api_key = open(file_path, "r").read()

agents_name_description = {}
topic = []


def main():
    with st.sidebar:
        st.header(
            "Lets start a discussion! Enter a topic you want to discuss and create 3 agents. (Chat input is going to be available after creating agents)")
        create_topic()
        create_agent_name_and_description()
    if st.session_state.stage_agent >= 4:
        # agents_db(agents_name_description)
        chat_db(agents_name_description)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "stage_agent" not in st.session_state:
    st.session_state.stage_agent = 0

if "disabled_topic" not in st.session_state:
    st.session_state["disabled_topic"] = False

if "disabled_chat_input" not in st.session_state:
    st.session_state["disabled_chat_input"] = True

if "disabled_finish_button" not in st.session_state:
    st.session_state["disabled_finish_button"] = False

if "disabled_agent_1" not in st.session_state:
    st.session_state["disabled_agent_1"] = False

if "disabled_agent_description_1" not in st.session_state:
    st.session_state["disabled_agent_description_1"] = False

if "disabled_agent_description_2" not in st.session_state:
    st.session_state["disabled_agent_description_2"] = False

if "disabled_agent_description_3" not in st.session_state:
    st.session_state["disabled_agent_description_3"] = False

if "disabled_agent_2" not in st.session_state:
    st.session_state["disabled_agent_2"] = False

if "disabled_agent_3" not in st.session_state:
    st.session_state["disabled_agent_3"] = False

if "disabled_add_button_1" not in st.session_state:
    st.session_state["disabled_add_button_1"] = False

if "disabled_add_button_2" not in st.session_state:
    st.session_state["disabled_add_button_2"] = False


def disable_topic():
    st.session_state["disabled_topic"] = True


def disable_chat_input():
    st.session_state["disabled_chat_input"] = False


def disable_finish_button():
    st.session_state["disabled_finish_button"] = True


def disable_agent_1():
    st.session_state["disabled_agent_1"] = True


def disable_agent_description_1():
    st.session_state["disabled_agent_description_1"] = True


def disable_agent_description_2():
    st.session_state["disabled_agent_description_2"] = True


def disable_agent_description_3():
    st.session_state["disabled_agent_description_3"] = True


def disable_agent_2():
    st.session_state["disabled_agent_2"] = True


def disable_agent_3():
    st.session_state["disabled_agent_3"] = True


def disable_add_button_1():
    st.session_state["disabled_add_button_1"] = True


def disable_add_button_2():
    st.session_state["disabled_add_button_2"] = True


def set_state():
    st.session_state.stage_agent += 1


def chat_db(agents_dict):
    names = list(agents_dict.keys())
    description = list(agents_dict.values())

    if prompt := st.chat_input("Type something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with (st.chat_message("assistant")):
            message_placeholder = st.empty()
            message_placeholder_feedback = st.empty()
            full_response = ""

            query = collection.query(query_texts=[prompt])
            for inner_list in query["documents"]:
                text = ", ".join(inner_list)
            # role system, wo der text ist funktioniert viel besser, als assistant
            for response in client.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    temperature=0,
                    messages=[{"role": "system", "content": text},
                              {"role": "user",
                               "content": prompt + f". I want to hear the opinions of {names[0]}, {names[1]}, {names[2]}"},
                              {"role": "assistant",
                               "content":
                                   f"Analyze the prompt, on who is supposed to answer. It may not be you, who needs to answer. You name is: {names[0]}. Your description is: {description[0]}."
                                   f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can, "
                                   f"but you are open to new opinions."
                                   f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                   f" Always reply with your name, For example: 'your name': ... "},
                              {"role": "assistant",
                               "content": f"Analyze the prompt, on who is supposed to answer. It may not be you, who needs to answer. You name is: {names[1]}. Your description is: {description[1]}."
                                          f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can,"
                                          f"but you are open to new opinions."
                                          f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                          f"Always reply with your name, For example: 'your name': ... "},
                              {"role": "assistant",
                               "content": f"Analyze the prompt, on who is supposed to answer. It may not be you, who needs to answer. You name is: {names[2]}. Your description is: {description[2]}."
                                          f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can,"
                                          f"but you are open to new opinions."
                                          f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                          f"Always reply with your name, For example: 'your name': ... "}],
                    stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                ids = 0
                if not collection.get(str(ids)):
                    collection.add(
                        documents=[full_response],
                        ids=[str(ids)]
                    )
                    ids += 1
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            message_placeholder_feedback.markdown("Feedback for the conversation from GPT: " + feedback(full_response))
            st.session_state.messages.append({"role": "assistant", "content": full_response})


def create_topic():
    global topic
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state["disabled_topic"], on_change=disable_topic)
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry}")


def feedback(response_agents):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant",
                   "content": f"You are going to evaluate this discussion on a scale from 1 to 10: {response_agents}, based on this factors: Relevance to Participants: A discussion is more likely to be engaging if it is relevant to the participants. Ensuring that the topic aligns with the interests, experiences, and concerns of those involved can enhance interest."
                              "Clear Purpose and Goals: Participants are more likely to find a discussion interesting if it has a clear purpose and specific goals. Knowing why they are engaging in the discussion and what they hope to achieve can maintain focus and interest."
                              "Active Participation: A dynamic discussion with active participation from all involved parties tends to be more interesting. Encouraging contributions, asking thought-provoking questions, and fostering a collaborative environment can enhance engagement."
                              "Diversity of Perspectives: Including a variety of perspectives and opinions can make a discussion more interesting. Differing viewpoints contribute to a more enriching and dynamic conversation."
                              "Well-Structured Facilitation: Effective facilitation helps guide the discussion in a coherent and organized manner. A well-structured discussion with clear transitions, relevant prompts, and appropriate time management can contribute to interest."
                              "Open-mindedness and Respect: Participants are more likely to stay engaged when they feel their opinions are respected and that there is an open-minded atmosphere. Fostering a respectful and inclusive environment encourages active participation and interest."
                              "Relevant Examples and Analogies: Providing concrete examples or relatable analogies can make complex or abstract concepts more interesting. Real-world applications help participants connect with the discussion content."
                              "Timeliness: A timely discussion that addresses current events or recent developments in a field can be more interesting. Staying relevant to the current context adds value and immediacy to the conversation."
                              "Engaging Communication Style: The way the discussion is communicated, including the use of language, tone, and expression, can impact interest. A conversational and engaging communication style can capture and maintain attention."
                              "Problem-Solving or Decision-Making Opportunities: Discussions that involve problem-solving or decision-making aspects can be inherently more interesting. Participants may feel more invested when they have a role in shaping outcomes."
                              "Interactive Elements: Incorporating interactive elements, such as polls, breakout sessions, or group activities, can break up the discussion and keep participants engaged."
                              "Follow-up and Action Plans: Discussions are more likely to be interesting if there are clear follow-up actions or plans. Knowing that the discussion has tangible outcomes or next steps can motivate participants to stay engaged"}]
    )
    return response['choices'][0]['message']['content']


def create_agent_name_and_description():
    if st.session_state.stage_agent == 0:
        st.button('Add agent', on_click=set_state)

    if st.session_state.stage_agent >= 1:
        agent_name_1 = st.text_input('Name',
                                     on_change=disable_agent_1,
                                     disabled=st.session_state["disabled_agent_1"])
        st.write(f"Name of Agent 1: {agent_name_1}")
        agent_description_1 = st.text_input("Description",
                                            on_change=set_state and disable_agent_description_1,
                                            disabled=st.session_state["disabled_agent_description_1"],
                                            key="agent_1")
        st.write(f"Description of Agent {agent_name_1}: {agent_description_1}")
        agents_name_description[f"{agent_name_1}"] = f"{agent_description_1}"

        if agent_name_1 and agent_description_1:
            st.button('Add agent', disabled=st.session_state["disabled_add_button_1"], on_click=set_state, key="")
            disable_add_button_1()

            if st.session_state.stage_agent >= 2:
                agent_name_2 = st.text_input('Name',
                                             on_change=disable_agent_2,
                                             disabled=st.session_state["disabled_agent_2"],
                                             key="name_agent_2")
                st.write(f"Name of Agent 2: {agent_name_2}")
                agent_description_2 = st.text_input("Description",
                                                    on_change=set_state and disable_agent_description_2,
                                                    disabled=st.session_state["disabled_agent_description_2"],
                                                    key="agent_2")
                st.write(f"Description of Agent {agent_name_2}: {agent_description_2}")
                agents_name_description[f"{agent_name_2}"] = f"{agent_description_2}"

                if agent_name_2 and agent_description_2:
                    st.button('Add agent', disabled=st.session_state["disabled_add_button_2"], on_click=set_state,
                              key=4)
                    disable_add_button_2()

                    if st.session_state.stage_agent >= 3:
                        agent_name_3 = st.text_input('Name',
                                                     on_change=disable_agent_3,
                                                     disabled=st.session_state["disabled_agent_3"],
                                                     key="name_agent_3")
                        st.write(f"Name of Agent 3: {agent_name_3}")
                        agent_description_3 = st.text_input("Description",
                                                            on_change=set_state and disable_agent_description_3,
                                                            disabled=st.session_state[
                                                                "disabled_agent_description_3"],
                                                            key="agent_3")
                        st.write(f"Description of Agent {agent_name_3}: {agent_description_3}")
                        agents_name_description[f"{agent_name_3}"] = f"{agent_description_3}"
                        if agent_name_3 and agent_description_3:
                            st.button('Start', disabled=st.session_state["disabled_finish_button"], key="finish_button",
                                      on_click=set_state)
                            disable_finish_button()


if __name__ == "__main__":
    main()
