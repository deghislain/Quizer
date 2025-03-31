import json
import unittest
import logging
from quiz_helper import Test, Answer, Question

string_questions = """
 [
        {
            "question": "What are large language models?",
            "answers": {
                "A": "responseA",
                "B": "responseB",
                "C": "responseC"
            },
            "solution": "A"
        }
]

"""


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




