import streamlit as st
from document_helper import PDFVectorDBLoader
from langchain_openai import ChatOpenAI
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    label = "Upload multiple PDF document here"
    uploaded_files = st.file_uploader(label, type=['pdf'], accept_multiple_files=False, key=None, help=None,
                                      on_change=None,
                                      args=None, kwargs=None, disabled=False, label_visibility="visible")
    if uploaded_files:
        logging.info(f"Document {uploaded_files.name} successfully loaded")
        vdb = PDFVectorDBLoader(uploaded_files)
        pdf_text_content = vdb.get_pdf_content()



if __name__ == "__main__":
    main()
