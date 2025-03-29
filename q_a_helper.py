from pydantic import Field


class Answer:
    choice_one: str = Field(description="Answer choice one")
    choice_two: str = Field(description="Answer choice two")
    choice_three: str = Field(description="Answer choice three")
    solution: str = Field(description="Solution to the question")


class Question:
    question: str = Field(description="Question to be sent to the user")
    answers: Answer = Field(description="Multiple choices answers to the question")
