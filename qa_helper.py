from pydantic import Field
from typing import List
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Answer:
    choice_one: str = Field(description="Answer choice one")
    choice_two: str = Field(description="Answer choice two")
    choice_three: str = Field(description="Answer choice three")
    solution: str = Field(description="Solution to the question")


class Question:
    question: str = Field(description="Question to be sent to the user")
    answers: Answer = Field(description="Multiple choices answers to the question")


class Test:
    questions: List[Question] = Field(description="List of questions with answers")

    def __init__(self, json_questions):
        self.test_questions = []
        self.json_questions = json_questions

    def _retrieve_questions(self) -> List[Question]:
        try:
            json_resp = json.loads(self.json_questions)
            questions = json_resp["questions"]
            for count in range(len(questions)):
                question = questions[count]["question"]
                answers = questions[count]["answers"]
                answer = Answer()
                answer.choice_one = answers['A']
                answer.choice_two = answers['B']
                answer.choice_three = answers['C']
                answer.solution = answers['solution']
                q = Question()
                q.question = question
                q.answers = answer
                self.test_questions.append(q)
        except Exception as ex:
            logging.error(f"Error while parsing json questions: {ex}")

        return self.test_questions

    def generate_questions(self) -> List[Question]:
        return self._retrieve_questions()


def create_test(json_questions) -> Test:
    test = Test(json_questions)
    questions = test.generate_questions()
    test.test_questions = questions
    return test
