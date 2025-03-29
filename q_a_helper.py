from pydantic import Field
from typing import List


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

    def __init__(self):
        self.test_questions = []

    def _create_test(self, json_questions) -> List[Question]:
        return self.test_questions


def create_test(json_questions) -> Test:
    test = Test()

    return test
