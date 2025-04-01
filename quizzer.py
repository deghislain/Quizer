import streamlit as st
from quiz_document_helper import load_document
from langchain_openai import ChatOpenAI
from quz_prompt import get_prompt
from langchain.schema import HumanMessage
from quiz_helper import create_test
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
llm = ChatOpenAI(model="granite3.1-dense:2b", temperature=0, base_url="http://localhost:11434/v1", api_key="ollama")


def generate_questions(pdf_text_content: str, topic: str, number: str) -> str:
    """
    Generate multiple-choice questions from a provided text document using an AI model.

    :param pdf_text_content: Content of the PDF document as string.
    :param topic: Main topic related to the document.
    :param number: Indicator for the question set (e.g., '1', '2', ...).
    :return: JSON formatted string containing generated multiple-choice questions.
    """
    if not pdf_text_content:
        logging.warning("No text content to process. Returning empty JSON.")
        return "{}"
    try:
        # Generate prompt based on the provided PDF text content, topic, and number
        query = get_prompt(pdf_text_content, topic, number)

        # Prepare the message to be sent to the AI model
        message = HumanMessage(content=query)

        current_time_seconds_start = time.time()

        # Invoke the AI model to generate the question
        question_json = llm.invoke([message]).content.strip()

        current_time_seconds_end = time.time()
        duration = current_time_seconds_end - current_time_seconds_start
        logging.info(f"Model Response Time in seconds: {duration}")
        logging.info(f"*Generated question*: {question_json}")

        return question_json

    except Exception as e:
        logging.error(f"An error occurred while generating questions: {e}")
        return "{}"


if __name__ == "__main__":
    pdf_text_content = load_document()
    if pdf_text_content:
        topic = st.text_input(":blue[Enter a topic:]", placeholder="eg AI")
        number = st.text_input(":blue[Enter the number of question per test:]", placeholder="eg 5")
        btn_submit = st.button("Submit")
        if btn_submit and topic and number:
            question_json = generate_questions(pdf_text_content, topic, str(number))
            if question_json:
                logging.info(f"Generated question: {question_json}")
                test = create_test(question_json)
                logging.info("Test successfully created")
            st.write(question_json)
