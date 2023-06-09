'''
Date: 2023-05-10 15:19:16
Author: Bruce
Description: front end page
'''

import streamlit as st
from streamlit_chat import message
from typing import Set

# Import Custome Function
from backend.core import run_llm


def create_source_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_lists = list(source_urls)
    sources_lists.sort()
    sources_string = "sources:\n"
    for index, source in enumerate(sources_lists):
        sources_string += f"{index + 1}. {source}\n"
    return sources_string

st.header("LangChain Header")

prompt = st.text_input("Prompt", placeholder="Enter your prompt")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if prompt:
    with st.spinner("Generating response..."):
        # Just for test
        # import time
        # time.sleep(10)

        generated_response = run_llm(query=prompt)
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])
        # print(generated_response)
        formatted_response = f"{generated_response['result']} \n\n {create_source_string(sources)}"

        # Append the prompt
        st.session_state["user_prompt_history"].append(prompt)
        # Append the answer
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"]):
        message(user_query, is_user=True)
        message(generated_response)