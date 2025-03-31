from PyPDF2 import PdfReader
import logging
import streamlit as st

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def load_document():
    """
    Function to upload a PDF document and extract its text content.
    :return: Text content of the uploaded PDF or an empty string if no file is uploaded.
    """
    label = ":blue[Upload a PDF document here]"
    uploaded_files = st.file_uploader(label, type=['pdf'], accept_multiple_files=False)
    pdf_text_content = ""
    if uploaded_files:
        try:
            logging.info(f"Document {uploaded_files.name} successfully loaded")
            pvdb = PDFVectorDBLoader(uploaded_files)
            pdf_text_content = pvdb.get_pdf_content()
        except Exception as e:
            logging.error(f"Error processing PDF: {e}")
            pdf_text_content = ""

    return pdf_text_content


class PDFVectorDBLoader:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def _extract_text_from_pdf(self):
        logging.info("************In _extract_text_from_pdf: Extracting the content of the pdf")
        text = ""
        if self.pdf_file is not None:
            reader = PdfReader(self.pdf_file)
            for page in reader.pages:
                text = text + page.extract_text()
        return text

    def get_pdf_content(self):
        return self._extract_text_from_pdf()
