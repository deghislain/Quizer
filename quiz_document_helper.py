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
    """
           A class designed to extract text content from PDF documents.

           This class leverages the PyPDF2 library to read and extract text from PDF files.
           """

    def __init__(self, pdf_file_path: str):
        """
        Initializes the PDFVectorDBLoader instance with a PDF file path.

        :param pdf_file_path: Path to the PDF file.
        """
        self.pdf_file_path = pdf_file_path
        logging.debug("PDFVectorDBLoader initialized with file path: %s", self.pdf_file_path)

    def _extract_text_from_pdf(self) -> str:
        """
        Internal method to extract text from the PDF file.

        :return: Extracted text content as a string.
        """
        if not self.pdf_file_path:
            logging.warning("No PDF file path provided. Returning empty string.")
            return ""

        logging.info("************In _extract_text_from_pdf: Extracting the content of the pdf")
        try:
            text = ""
            if self.pdf_file_path is not None:
                reader = PdfReader(self.pdf_file_path)
                for page in reader.pages:
                    text = text + page.extract_text()

        except Exception as e:
            logging.error(f"Error extracting text from PDF: {e}")
            return ""

        return text

    def get_pdf_content(self) -> str:
        """
        Retrieves and returns the text content of the PDF file.

        :return: Text content of the PDF as a string.
        """
        logging.info("Calling get_pdf_content method")
        return self._extract_text_from_pdf()

