Quizer Application: PDF Knowledge Test

Welcome to Quizer, a user-friendly application specifically designed to evaluate your comprehension of a chosen PDF document's content.
By leveraging advanced AI technologies, Quizer generates multiple-choice questions (MCQs) based on the PDF's extractable information, 
offering an interactive learning experience.

Overview

Quizer empowers users to:

    Upload a PDF document for content analysis.
    Automatically generate an MCQ test from the document's key points.
    Evaluate their understanding and knowledge through interactive quiz sessions.

Features

Quizer comprises four core modules, each contributing to its robust functionality:

    quiz_document_helper: A dedicated module focused on extracting essential content from uploaded PDF documents, ensuring a focused and relevant quiz generation.
    quiz_helper: This module is equipped with algorithms to craft precise and educational MCQs, leveraging the extracted content effectively.
    quiz_prompt: Houses standardized interaction prompts, facilitating consistent communication with the AI model for question generation.
    quizer: The central orchestrator, managing user interactions, model integrations, and overall application flow seamlessly.

Technologies Utilized

    langchain: Facilitates the smart orchestration and interaction among AI models and data sources, central to Quizer's automated question-generation process.
    Granite Model: A sophisticated large language model, integral to comprehending content and formulating accurate and diverse MCQs.
    ollama: Supported for local model execution, ensuring controlled and efficient performance environments.
    streamlit: semplifies the implementation of the GUI

Getting Started

    Installation: Ensure you have the required dependencies installed, including langchain, Granite, and ollama`.
    Usage:
        Navigate to the project's root directory.
        Execute the following command streamlit run quizzer.py

Detailed installation and execution instructions are available in the project's documentation or can be requested separately.