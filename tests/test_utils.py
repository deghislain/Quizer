string_questions = """{
     "questions": [
            {
          "question": "What are large language models?",
          "answers": [
            "A) responseA",
            "B) responseB",
            "C) responseC"
          ],
          "solution": "B"
        }
    ]
}
"""

invalid_format_questions = """
 [
        {
            "question": "What are large language models?",
            "answers" {
                "A": "responseA",
                "B": "responseB",
                "C": "responseC"
            },
            "solution": "A"
        }
]
"""

invalid_questions_structure = """
 [
        {
            "question": "What are large language models?",
            "answers": {
                "A": "responseA",
                "B": "responseB",
                "C": "responseC"
            },
            
        }
]
"""