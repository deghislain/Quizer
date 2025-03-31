import streamlit as st
from document_helper import load_document
from langchain_openai import ChatOpenAI
from qa_prompt import get_prompt
from langchain.schema import HumanMessage
from qa_helper import create_test
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
llm = ChatOpenAI(model="granite3-dense:latest", temperature=0, base_url="http://localhost:11434/v1", api_key="ollama")


def generate_questions(pdf_text_content: str, topic: str, number: str):
    question_json = ""
    if pdf_text_content:
        query = get_prompt(pdf_text_content, topic, number)
        message = HumanMessage(content=query)
        current_time_seconds_start = time.time()
        question_json = llm.invoke([message]).content.strip()
        current_time_seconds_End = time.time()
        duration = current_time_seconds_End - current_time_seconds_start
        logging.info(f"Model Response Time in seconds: {duration}")
        logging.info(f"*****************************Generated question: {question_json}")
    return question_json


if __name__ == "__main__":
    pdf_text_content = load_document()
    if pdf_text_content:
        topic = st.text_input(":blue[Enter a topic:]", placeholder="eg AI")
        number = st.text_input(":blue[Enter the number of question per test:]", placeholder="eg 5")
        btn_submit = st.button("Submit")
        if btn_submit and topic and number:
            question_json = generate_questions(pdf_text_content, topic, str(number))
            logging.info(f"Generated question: {question_json}")
            test = create_test(question_json)
            logging.info("Test successfully created")
            st.write(question_json)

