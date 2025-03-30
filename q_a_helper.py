from pydantic import Field, BaseModel
from typing import List, Any


class Answer(BaseModel):
    choice_one: str = Field(description="Answer choice one")
    choice_two: str = Field(description="Answer choice two")
    choice_three: str = Field(description="Answer choice three")
    solution: str = Field(description="Solution to the question")


class Question(BaseModel):
    question: str = Field(description="Question to be sent to the user")
    answers: Answer = Field(description="Multiple choices answers to the question")


class Test(BaseModel):
    questions: List[Question] = Field(description="List of questions with answers")

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self.test_questions = []

    def _create_test(self, json_questions) -> List[Question]:
        return self.test_questions


def create_test(json_questions) -> Test:
    test = Test()

    return test
