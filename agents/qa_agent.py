from transformers import pipeline

class QnAAgent:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering")

    def answer_question(self, question, context):
        response = self.qa_pipeline(question=question, context=context)
        return response["answer"]
