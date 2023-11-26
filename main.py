import openai
import streamlit as st

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

agents_name_description = {}
topic = []


def main():
    with st.sidebar:
        st.header(
            "Lets start a discussion! Enter a topic you want to discuss and create 3 agents. (Chat input is going to be available after creating agents)")
        create_topic()
        create_agent_name_and_description()
    if st.session_state.stage_agent >= 4:
        # disable_chat_input()
        #agents(agents_name_description)
        chat(agents_name_description)
    # st.chat_input("Say something", disabled=st.session_state["disabled_chat_input"])


if "messages" not in st.session_state:
    st.session_state.messages = []

if 'stage_agent' not in st.session_state:
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


# def chat(agents_dict):
#     names = list(agents_dict.keys())
#     description = list(agents_dict.values())
#     # temperature funktioniert irgendwie nicht. Assistant funktioniert irgendwie nicht, aber System läuft besser.
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         # temperature=0,
#         messages=[
#             {"role": "system",
#              "content": f"name: {names[0]}.  description: {description[0]}. topic: {topic}"},
#             {"role": "system",
#              "content": f"name: {names[1]}. description: {description[1]}. topic: {topic}"},
#             {"role": "system",
#              "content": f"name: {names[2]}. description: {description[2]}. topic: {topic}"}
#         ]
#     )
#     st.session_state.messages.append(response['choices'][0]['message']['content'])
#
#     prompt = st.chat_input("Initialize the conversation!")
#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)
#
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             full_response = ""
#             for response in openai.ChatCompletion.create(
#                     model="gpt-3.5-turbo",
#                     messages=[
#                         {"role": m["role"], "content": m["content"]}
#                         for m in st.session_state.messages
#                     ],
#                     stream=True,
#             ):
#                 full_response += (response.choices[0].delta.content or "")
#                 message_placeholder.markdown(full_response + "▌")
#             message_placeholder.markdown(full_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})

def chat(agents_dict):
    names = list(agents_dict.keys())
    description = list(agents_dict.values())

    # Construct system messages for each agent
    system_messages = [
        {"role": "system", "content": f"name: {names[i]}.  description: {description[i]}. topic: {topic}"}
        for i in range(len(names))
    ]

    # Call OpenAI API to get initial responses
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=system_messages
    )
    st.session_state.messages.append(response['choices'][0]['message'])

    prompt = st.chat_input("Initialize the conversation!")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages,
                    stream=True,
            ):
                full_response += (response.choices[0].delta.content or "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})




def agents(agents_dict):
    names = list(agents_dict.keys())
    description = list(agents_dict.values())
    # temperature funktioniert irgendwie nicht. Assistant funktioniert irgendwie nicht, aber System läuft besser.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # temperature=0,
        messages=[
            {"role": "assistant",
             "content": f"name: {names[0]}.  description: {description[0]}. topic: {topic}"},
            {"role": "assistant",
             "content": f"name: {names[1]}. description: {description[1]}. topic: {topic}"},
            {"role": "assistant",
             "content": f"name: {names[2]}. description: {description[2]}. topic: {topic}"}
        ]
    )
    st.write(response['choices'][0]['message']['content'])


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
