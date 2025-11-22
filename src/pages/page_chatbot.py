import streamlit as st
import os

st.set_page_config(page_title="Chatbot", page_icon="💬")


INITIAL_ASSISTANT_MSG = (
    "Olá sou a SofIA e estou aqui para te ajudar com suas finanças. 😁"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Mock data"},
        {"role": "assistant", "content": INITIAL_ASSISTANT_MSG},
    ]

st.title("SofIA")

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_text := st.chat_input("aaaaaaaaaaaaa"):
    # add user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # call LLM
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            assistant_text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            st.markdown(assistant_text)

            # response = client.chat.completions.create(
            #     model="gpt-4.1-mini",  # ou outro modelo que você tiver
            #     messages=st.session_state.messages,
            # )
            # assistant_text = response.choices[0].message.content
            # st.markdown(assistant_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text}
    )
