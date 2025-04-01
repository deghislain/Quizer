import unittest
import logging
from quiz_helper import Test, Answer, Question, create_test
from test_utils import string_questions, invalid_format_questions, invalid_questions_structure


class TestProcessTestCreation(unittest.TestCase):

    def setUp(self):
        # Set up logging to avoid output during tests
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        # Reset logging after each test
        logging.disable(logging.NOTSET)

    def test_init_with_questions(self):
        # Test initialization with a valid file path

        test = Test(string_questions)
        self.assertEqual(test.string_questions, string_questions)

    def test_init_missing_questions(self):
        # Test initialization with a valid file path

        test = Test(string_questions)
        self.assertEqual(test.string_questions, string_questions)

    def test_generate_questions_correct_json_questions(self):
        list_questions = []
        test = Test(string_questions)
        answer = Answer(choice_one='responseA', choice_two='responseB', choice_three='responseC', solution='A')
        question = Question(answers=answer, question='What are large language models?')

        list_questions.append(question)

        generated_questions = test.generate_questions()

        self.assertEqual(generated_questions, list_questions)

    def test_generate_questions_invalid_json_format(self):
        list_questions = []
        test = Test(invalid_format_questions)

        generated_questions = test.generate_questions()

        self.assertEqual(generated_questions, list_questions)

    def test_generate_questions_invalid_json_missing_solution(self):
        list_questions = []
        test = Test(invalid_questions_structure)

        generated_questions = test.generate_questions()

        self.assertEqual(generated_questions, list_questions)

    def test_create_test_correct_input(self):
        list_questions = []
        test = Test(string_questions)
        answer = Answer(choice_one='responseA', choice_two='responseB', choice_three='responseC', solution='A')
        question = Question(answers=answer, question='What are large language models?')

        list_questions.append(question)

        test.test_questions = list_questions

        created_test = create_test(string_questions)

        self.assertEqual(test.test_questions, created_test.test_questions)

    def test_create_test_incorrect_input(self):
        list_questions = []
        test = Test(invalid_format_questions)

        test.test_questions = list_questions

        created_test = create_test(invalid_format_questions)

        self.assertEqual(test.test_questions, created_test.test_questions)

    def test_create_test_incorrect_json_input_structure(self):
        list_questions = []
        test = Test(invalid_questions_structure)

        test.test_questions = list_questions

        created_test = create_test(invalid_questions_structure)

        self.assertEqual(test.test_questions, created_test.test_questions)





