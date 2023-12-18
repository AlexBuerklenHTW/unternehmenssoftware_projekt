import logging
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

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            query = collection.query(query_texts=[prompt])
            for inner_list in query["documents"]:
                text = ", ".join(inner_list)
            # role system, wo der text ist funktioniert viel besser, als assistant
            logging.info(query)
            for response in client.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    temperature=0,
                    messages=[{"role": "system", "content": text},
                              {"role": "system",
                               "content": f"You take the role of: {names[0]}. Your description is: {description[0]}."
                                          f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can."
                                          f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                          f" Always reply with your name, For example: 'your name': ... "},
                              {"role": "system",
                               "content": f"You take the role of: {names[1]}. Your description is: {description[1]}."
                                          f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can."
                                          f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                          f"Always reply with your name, For example: 'your name': ... "},
                              {"role": "system",
                               "content": f"You take the role of: {names[2]}. Your description is: {description[2]}."
                                          f"The topic you going to discuss about: {topic}. You only gonna take position for your description and defend your position as best as you can."
                                          f"The point is, that the discussion should not be one sided, more back and forth. You going to answer in the language of the user prompt."
                                          f"Always reply with your name, For example: 'your name': ... "},
                              {"role": "user",
                               "content": prompt}],
                    stream=True,
            ):
                logging.info(response)
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
            st.session_state.messages.append({"role": "assistant", "content": full_response})


def create_topic():
    global topic
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state["disabled_topic"], on_change=disable_topic)
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry}")


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
