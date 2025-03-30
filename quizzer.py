import streamlit as st
from document_helper import PDFVectorDBLoader
from langchain_openai import ChatOpenAI
from qa_prompt import get_prompt
from langchain.schema import SystemMessage, HumanMessage
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
llm = ChatOpenAI(model="granite3-dense:8b", temperature=0, base_url="http://localhost:11434/v1", api_key="ollama")


def load_document():
    label = ":blue[Upload a PDF document here]"
    uploaded_files = st.file_uploader(label, type=['pdf'], accept_multiple_files=False, key=None, help=None,
                                      on_change=None,
                                      args=None, kwargs=None, disabled=False, label_visibility="visible")
    pdf_text_content = ""
    if uploaded_files:
        logging.info(f"Document {uploaded_files.name} successfully loaded")
        vdb = PDFVectorDBLoader(uploaded_files)
        pdf_text_content = vdb.get_pdf_content()

    return pdf_text_content


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
        if topic and number:
            question_json = generate_questions(pdf_text_content, topic, str(number))
            logging.info(f"Generated question: {question_json}")

            st.write(question_json)
