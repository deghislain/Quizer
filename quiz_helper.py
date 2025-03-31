import json
from typing import List
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class Answer:
    choice_one: str
    choice_two: str
    choice_three: str
    solution: str


@dataclass
class Question:
    question: str
    answers: Answer


class Test:
    def __init__(self, json_questions: str):
        """
        Initializes the Test class with the path to a JSON file containing questions and answers.

        :param json_questions: Path to the JSON file containing the questions and answers.
        """
        self.json_file_path = json_questions
        self.test_questions: List[Question] = []

    def _process_questions(self, json_questions: List[dict]) -> List[Question]:
        """
        Processes the list of question dictionaries into a list of Question objects.

        :param json_questions: List of question dictionaries.
        :return: List of Question objects.
        """
        processed_questions = []

        for question_data in json_questions:
            question_text = question_data["question"]
            answers = {
                "A": question_data.get("answer_A", ""),
                "B": question_data.get("answer_B", ""),
                "C": question_data.get("answer_C", ""),
                "solution": question_data.get("solution", "")
            }

            answer_obj = Answer(choice_one=answers["A"], choice_two=answers["B"], choice_three=answers["C"],
                                solution=answers["solution"])
            question_obj = Question(question=question_text, answers=answer_obj)
            processed_questions.append(question_obj)

        return processed_questions

    def generate_questions(self) -> List[Question]:
        """
        Retrieves and processes the questions and answers from the JSON file into a list of Question objects.

        :return: List of Question objects.
        """
        json_questions = json.loads(self.json_file_path)
        return self._process_questions(json_questions)


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
        return Test([])  # Return an empty Test object in case of failure
