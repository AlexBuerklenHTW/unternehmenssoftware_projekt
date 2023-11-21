# step-back-prompting
# testen, ob name wirklich unterschied macht
# streamlit website anschauen
# chromadb anschauen
# max_tokens als limit setzen

import streamlit as st

def main():
    st.write(st.session_state)
    create_topic()
    create_agent()
    #add_agent()


topic = []
agents = []
counter = 0

if "disabled_topic" not in st.session_state:
    st.session_state["disabled_topic"] = False

if "disabled_agent" not in st.session_state:
    st.session_state["disabled_agent"] = False



def disable_topic():
    st.session_state["disabled_topic"] = True

def disable_agent():
    st.session_state["disabled_agent"] = True

def enable_agent():
    st.session_state["disabled_agent"] = False

# def add_agent():
#     button = st.button("click here to add agent")
#     if button:
#         create_agent()


def create_topic():
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state["disabled_topic"], on_change=disable_topic)
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry}")


def create_agent():
    global counter
    agent_entry = st.text_input("Enter name of agent:", disabled=st.session_state["disabled_agent"], on_change=disable_agent, key=counter)
    counter += 1
    if agent_entry:
        agents.append(agent_entry)
        st.write(f"Agent name: {agent_entry}")
        button = st.button("click here to add agent")
        if button:
            enable_agent()
            create_agent()



if __name__ == "__main__":
    main()
