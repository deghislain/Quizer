import unittest
from unittest.mock import patch, MagicMock
from quiz_document_helper import PDFVectorDBLoader
import logging
from PyPDF2 import PdfReader


class TestPDFVectorDBLoader(unittest.TestCase):

    def setUp(self):
        # Set up logging to avoid output during tests
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        # Reset logging after each test
        logging.disable(logging.NOTSET)

    def test_init(self):
        # Test initialization with a valid file path
        pdf_file_path = 'test.pdf'
        loader = PDFVectorDBLoader(pdf_file_path)
        self.assertEqual(loader.pdf_file_path, pdf_file_path)

    def test_init_missing_file_path(self):
        # Test initialization with missing file path
        pdf_file_path = ''
        loader = PDFVectorDBLoader(pdf_file_path)
        self.assertEqual(loader.pdf_file_path, '')

    def test_extract_text_from_pdf_no_file_path(self):
        # Test _extract_text_from_pdf with no file path
        loader = PDFVectorDBLoader('')
        self.assertEqual(loader._extract_text_from_pdf(), '')

    @patch('PyPDF2.PdfReader')
    def test_extract_text_from_pdf_pdf_reader_exception(self, mock_PdfReader):
        # Test _extract_text_from_pdf with a PdfReader exception
        mock_PdfReader.side_effect = Exception('Test exception')
        loader = PDFVectorDBLoader('test.pdf')
        self.assertEqual(loader._extract_text_from_pdf(), '')

    @patch('PyPDF2.PdfReader')
    def test_extract_text_from_pdf_valid(self, mock_PdfReader):
        # Test _extract_text_from_pdf with a valid PDF file
        mock_reader = MagicMock()
        mock_reader.pages = [MagicMock(), MagicMock()]
        mock_reader.pages[0].extract_text.return_value = 'Page 1'
        mock_reader.pages[1].extract_text.return_value = 'Page 2'
        mock_PdfReader.return_value = mock_reader
        loader = PDFVectorDBLoader('test.pdf')
        self.assertEqual(loader._extract_text_from_pdf(), 'Page1page2')

    @patch('PyPDF2.PdfReader')
    def test_extract_text_from_empty_pdf(self, mock_PdfReader):
        # Test _extract_text_from_pdf with an empty PDF file
        mock_reader = MagicMock()
        mock_reader.pages = [MagicMock(), MagicMock()]
        mock_reader.pages[0].extract_text.return_value = ''
        mock_PdfReader.return_value = mock_reader
        loader = PDFVectorDBLoader('empty.pdf')
        self.assertEqual(loader._extract_text_from_pdf(), '')

    @patch('PyPDF2.PdfReader')
    def test_extract_text_from_txt_failure(self, MockReader):
        MockReader.side_effect = Exception("Wrong format")

        loader = PDFVectorDBLoader('test.txt')
        result = loader.get_pdf_content()
        self.assertEqual(result, '')

    def test_get_pdf_content(self):
        # Test get_pdf_content method
        loader = PDFVectorDBLoader('test.pdf')
        self.assertEqual(loader.get_pdf_content(), loader._extract_text_from_pdf())


if __name__ == '__main__':
    unittest.main()
