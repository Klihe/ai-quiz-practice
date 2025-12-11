from langchain_openai import ChatOpenAI

from src.config.core import Config
from src.modules.models.llm.types import QuizReturn


class LLM(ChatOpenAI):
    def __init__(self) -> None:
        super().__init__(
            api_key=Config.OPENAI_API_KEY,
            model="gpt-4.1-2025-04-14"
        )

    def ask_quiz(self, question: str, user_answer: str, answer: str) -> QuizReturn:
        prompt = f"""
            You are an expert evaluator. Your task is to determine whether the "User Answer" expresses the same meaning as the "Correct Answer."

            Meaning is the key criterion.

            Guidelines for evaluation:
            - Focus on semantics, not exact wording.
            - Synonyms, paraphrasing, and reordered clauses are acceptable if the meaning stays equivalent.
            - Ignore tone, punctuation, and capitalization unless they change meaning.
            - Ignore filler words ("basically", "maybe", etc.) unless they change meaning.
            - If any essential part of the meaning differs, mark it as incorrect.

            Guidelines for hint creation:
            - The hint must guide the user toward the correct concept at a high level.
            - The hint must not reveal the correct answer verbatim.
            - Keep hints abstract and concept-oriented (e.g., "Consider the broader theme", "Think about the underlying principle", "Focus on the key relationship").

            Context:
            Question: {question}
            Correct Answer: {answer}
            User Answer: {user_answer}

            Language: {Config.LANGUAGE}
        """
        structured_llm = self.with_structured_output(QuizReturn)
        response = structured_llm.invoke(prompt)

        correct = response.get("correct")
        hint = response.get("hint")
        percentile = response.get("percentile")
        was_missing = response.get("was_missing")

        return QuizReturn(
            correct=correct,
            hint=hint,
            percentile=percentile,
            was_missing=was_missing
        )
