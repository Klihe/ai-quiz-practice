import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class LLM(ChatOpenAI):
    def __init__(self) -> None:
        super().__init__(
            api_key=os.getenv("API_KEY"),
            model="gpt-4.1-2025-04-14"
        )

    def validate(self, question: str, user_answer: str, answer: str) -> bool:
        prompt = f"""
            You are an expert evaluator. Your task: decide whether the “User Answer” conveys essentially the same meaning as the “Correct Answer.”

            You must consider:
            - Meaning / semantics rather than exact wording.
            - Synonyms, paraphrases, reordering of clauses, minor re-phrasings — these are fine **if** the meaning is equivalent.
            - Differences in style, punctuation, capitalization, but **not** differences that change the meaning (e.g. “All humans are mortal” vs “Some humans are mortal”).
            - Minor added/or removed filler words (e.g. “basically”, “in my opinion”, “maybe”, etc.) — ignore them if they don’t alter the core meaning.

            If the user answer and correct answer **do** convey the same meaning, reply exactly `true`.
            Otherwise, reply exactly `false`.

            Return only the word `true` or `false`, nothing else.

            Context:
            Question: {question}
            Correct Answer: {answer}
            User Answer: {user_answer}
        """
        response = self.invoke(prompt)
        return response.content.lower().strip() == "true"
