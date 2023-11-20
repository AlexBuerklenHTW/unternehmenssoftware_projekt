# step-back-prompting
# testen, ob name wirklich unterschied macht
# streamlit website anschauen
# chromadb anschauen
# max_tokens als limit setzen

import streamlit as st

topic = []
agents = []

if "disabled" not in st.session_state:
    st.session_state["disabled"] = False


def disable_topic():
    st.session_state["disabled"] = True


def disable_agent():
    st.session_state["disabled"] = True


def main():
    create_topic()
    create_agent()


def create_topic():
    topic_entry = st.text_input("Enter topic:", disabled=st.session_state.disabled, on_change=disable_topic())
    if topic_entry:
        topic.append(topic_entry)
        st.write(f"Topic: {topic_entry} (If you want a new topic, than refresh the page)")


def create_agent():
    agent_entry = st.text_input("Enter name of agent:", disabled=st.session_state.disabled, on_change=disable_agent(), key="create_agent")
    if agent_entry:
        topic.append(agent_entry)
        st.write(f"Topic: {agent_entry} (If you want a new topic, than refresh the page)")


if __name__ == "__main__":
    main()
