from PyPDF2 import PdfReader
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


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
