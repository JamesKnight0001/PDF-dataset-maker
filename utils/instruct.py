import requests
import json
import random
from openai import OpenAI

client = OpenAI()

class agent:
    @classmethod
    def generate(cls, messages):
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=False,
        )
        if "choices" in stream:
            return stream['choices'][0]['message']['content']
        else:
            return None
    
    @classmethod
    def summarize(cls, title, text):
        chat = []
        instruct00 = """[
    {
        'question': 'question',
        'answer': 'answer'
    }
]"""

        instruct01 = f"""You are an AI made to create questions and the answers with the provided information.
Here is how you should respond:
{instruct00}
Important: The question and the answer is required to be a one liner."""

        chat.append({"role": "system", "content": instruct01})
        chat.append({"role": "user","content": f"Make me a list of questions, and answer.\nYour goal is to make the question and answer detailed and understandable, basically like a teacher and a student questioning and answering each other.\nMake sure to make the question specific. Like providing the equation, or examples.\nThe one reading this dataset will not understand if the information is not provided.\nThey will not get the information in the book. So do not make questions about this book.\nPlease format it as: {instruct00}\n\nHeres the Info for you to make the question and answers:\nInfo:\n{text}"})

        response = agent.generate(messages=chat)
        return response
        
        