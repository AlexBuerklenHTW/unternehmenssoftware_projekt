# step-back-prompting
# testen, ob name wirklich unterschied macht
# streamlit website anschauen
# chromadb anschauen
# max_tokens als limit setzen

import streamlit as st


def main():
    st.header("Lets start a discussion! Enter a topic you want to discuss and create up to 3 agents")
    create_topic()
    create_agent()


topic = []
agents = []

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if "disabled_topic" not in st.session_state:
    st.session_state["disabled_topic"] = False

if "disabled_agent_1" not in st.session_state:
    st.session_state["disabled_agent_1"] = False

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


def disable_agent_2():
    st.session_state["disabled_agent_2"] = True


def disable_agent_3():
    st.session_state["disabled_agent_3"] = True


def disable_add_button_1():
    st.session_state["disabled_add_button_1"] = True


def disable_add_button_2():
    st.session_state["disabled_add_button_2"] = True


def set_state():
    st.session_state.stage += 1


def create_topic():
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state["disabled_topic"], on_change=disable_topic)
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry}")


def create_agent():
    if st.session_state.stage == 0:
        st.button('Add agent', on_click=set_state)

    if st.session_state.stage >= 1:
        agent_name = st.text_input('Name', on_change=set_state and disable_agent_1, key="name_agent_1",
                                   disabled=st.session_state["disabled_agent_1"])
        st.write(f"Name of Agent 1: {agent_name}")
        agents.append(agent_name)
        if agent_name:
            st.button('Add agent', disabled=st.session_state["disabled_add_button_1"], on_click=set_state, key="")
            disable_add_button_1()

            if st.session_state.stage >= 2:
                agent_name = st.text_input('Name', on_change=set_state and disable_agent_2, key="name_agent_2",
                                           disabled=st.session_state["disabled_agent_2"])
                st.write(f"Name of Agent 2: {agent_name}")
                agents.append(agent_name)
                if agent_name:
                    st.button('Add agent', disabled=st.session_state["disabled_add_button_2"], on_click=set_state,
                              key=4)
                    disable_add_button_2()

                    if st.session_state.stage >= 3:
                        agent_name = st.text_input('Name', on_change=set_state and disable_agent_3, key="name_agent_3",
                                                   disabled=st.session_state["disabled_agent_3"])
                        st.write(f"Name of Agent 3: {agent_name}")
                        agents.append(agent_name)



if __name__ == "__main__":
    main()
