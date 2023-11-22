# step-back-prompting
# testen, ob name wirklich unterschied macht
# streamlit website anschauen
# chromadb anschauen
# max_tokens als limit setzen

import openai
import streamlit as st

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()



def main():
    # st.chat_input("Say something")
    with st.sidebar:
        st.header("Lets start a discussion! Enter a topic you want to discuss and create up to 3 agents")
        create_topic()
        create_agent_name()



topic = []
agents = {}

if 'stage_agent' not in st.session_state:
    st.session_state.stage_agent = 0

if "disabled_topic" not in st.session_state:
    st.session_state["disabled_topic"] = False

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
    #st.session_state.stage_description += 1


def agent(name):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"name: {name}."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def create_topic():
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state["disabled_topic"], on_change=disable_topic)
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry}")




def create_agent_name():
    if st.session_state.stage_agent == 0:
        st.button('Add agent', on_click=set_state)

    if st.session_state.stage_agent >= 1:
        agent_name_1 = st.text_input('Name',
                                     on_change=disable_agent_1,
                                     disabled=st.session_state["disabled_agent_1"])
        st.write(f"Name of Agent 1: {agent_name_1}")
        agent_name_1_description = st.text_input("Description",
                                                 on_change=set_state and disable_agent_description_1,
                                                 disabled=st.session_state["disabled_agent_description_1"],
                                                 key="agent_1")
        st.write(f"Description of Agent {agent_name_1}: {agent_name_1_description}")
        #agents.update({"agent_1": agent_name_1})
        #create_agent_description(agents.get("agent_1"))

        if agent_name_1 and agent_name_1_description:
            st.button('Add agent', disabled=st.session_state["disabled_add_button_1"], on_click=set_state, key="")
            disable_add_button_1()


            if st.session_state.stage_agent >= 2:
                agent_name_2 = st.text_input('Name',
                                             on_change=disable_agent_2,
                                             disabled=st.session_state["disabled_agent_2"],
                                             key="name_agent_2")
                st.write(f"Name of Agent 2: {agent_name_2}")
                agent_name_2_description = st.text_input("Description",
                                                         on_change=set_state and disable_agent_description_2,
                                                         disabled=st.session_state["disabled_agent_description_2"],
                                                         key="agent_2")
                st.write(f"Description of Agent {agent_name_2}: {agent_name_2_description}")

                if agent_name_2 and agent_name_2_description:
                    st.button('Add agent', disabled=st.session_state["disabled_add_button_2"], on_click=set_state,
                              key=4)
                    disable_add_button_2()

                    if st.session_state.stage_agent >= 3:
                        agent_name_3 = st.text_input('Name',
                                                     on_change=disable_agent_3,
                                                     disabled=st.session_state["disabled_agent_3"],
                                                     key="name_agent_3")
                        st.write(f"Name of Agent 3: {agent_name_3}")
                        agent_name_3_description = st.text_input("Description",
                                                                 on_change=set_state and disable_agent_description_3,
                                                                 disabled=st.session_state[
                                                                     "disabled_agent_description_3"],
                                                                 key="agent_3")
                        st.write(f"Description of Agent {agent_name_3}: {agent_name_3_description}")
                        #agents.append(agent_name_3)


if __name__ == "__main__":
    main()
