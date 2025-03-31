example_response = """
{{
            "questions":{
                            { 
                                "question": "What are large language models?",
                                "answers": {
                                        "A": "Large language models are advanced artificial intelligence systems that take some input and generate humanlike text as a response."
                                        "B": "Large language models are AI protocols."
                                        "C": "Large language models are a type of neural networks."
                                },
                               "solution": "A"
                            },
                            { 
                                "question": "How does Large language models work?",
                                "answers": {
                                        "A": "They work by generating casual text"
                                        "B":  "They work by first analyzing vast amounts of data and creating an internal structure that models"
                                                the natural language data sets that they’re trained on."
                                        "C":  "Large language models just use statistic an internet to generate text"
                                },
                               "solution": "B"
                            }

        }}  
"""


def get_prompt(text_document, topic, number):
    return f""" 
        The following text document is about: {topic}.
        ---------------------
        {text_document}
        ---------------------
       You are a Cross-Disciplinary Subject Matter Expert with extensive knowledge spanning multiple domains. Given the 
       text document and not prior knowledge.
        Your task is to generate a list of {number} questions with answers.
        The instructions for this task are as follow:
        All generated questions must come from the provided text document content.
        You will return a response in json format. Each question must have 3 answers in the multiple choice question style.
        Only one response shall be correct. The correct answer shall be labeled as solution.
       

        Here are some examples of questions with their respective answers and solutions in json schema:

        {example_response}

"""
