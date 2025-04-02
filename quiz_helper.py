import json
from typing import List
from dataclasses import dataclass
import logging
import streamlit as st

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class Answer:
    choice_one: str
    choice_two: str
    choice_three: str



@dataclass
class Question:
    question: str
    answers: Answer
    solution: str


class Test:
    def __init__(self, string_questions: str):
        """
        Initializes the Test class with the path to a JSON file containing questions and answers.

        :param string_questions: json string containing the questions and answers.
        """
        self.string_questions = string_questions
        self.test_questions: List[Question] = []
        self.score = 0
        self.current_question_index = 0

    def _process_questions(self) -> List[Question]:
        logging.info("_process_questions*********************START")
        """
        Processes the list of question dictionaries into a list of Question objects.
        :return: List of Question objects.
        """
        processed_questions = []
        json_questions = json.loads(self.string_questions)
        questions = json_questions["questions"]
        for question_data in questions:
            question_text = question_data["question"]
            answers = question_data["answers"]

            answer_obj = Answer(choice_one=answers[0], choice_two=answers[1], choice_three=answers[2])

            question_obj = Question(question=question_text, answers=answer_obj, solution=question_data["solution"])
            processed_questions.append(question_obj)

        return processed_questions

    def _answer(self, q: Question) -> str:
        st.write(':blue[' + q.question + ']  5 points ')
        answers = q.answers
        resp_a = st.checkbox(answers.choice_one)
        resp_b = st.checkbox(answers.choice_two)
        resp_c = st.checkbox(answers.choice_three)

        if resp_a:
            return "A"
        elif resp_b:
            return "B"
        elif resp_c:
            return "C"
        else:
            return ""

    def get_user_answer(self, question: Question) -> str:

        return self._answer(question)

    def generate_questions(self) -> List[Question]:
        """
        Retrieves and processes the questions and answers from the JSON file into a list of Question objects.

        :return: List of Question objects.
        """
        try:
            json_questions = self._process_questions()
        except Exception as e:
            logging.error(f"Error creating test: {e}")
            return []

        return json_questions


def create_test(json_questions: str) -> Test:
    """
    Creates and initializes a Test object with questions loaded from a provided JSON list.

    :param json_questions: List of question dictionaries representing the test questions.
    :return: Initialized Test object with questions loaded.
    """
    try:
        test_obj = Test(json_questions)
        test_obj.test_questions = test_obj.generate_questions()
        return test_obj

    except Exception as e:
        logging.error(f"Error creating test: {e}")
        return Test("")  # Return an empty Test object in case of failure


def start_test(test=None):
    logging.info("In start_test*****************************")
    if "my_instance" in st.session_state:
        test = st.session_state.my_instance
    if test:
        logging.info(f"In start_test*****************************test from session {test}")
        index = test.current_question_index
        current_question = test.test_questions[index]
        user_answer = test.get_user_answer(current_question)
        test.current_question_index = index + 1
        if user_answer == current_question.solution:
            test.score += 5
        st.session_state.my_instance = test

