from langchain_openai import ChatOpenAI

from src.config import Config
from src.const import Const
from src.modules.models.llm.types import QuizReturn


class LLM(ChatOpenAI):
    def __init__(self) -> None:
        super().__init__(
            api_key=Config.OPENAI_API_KEY,
            model="gpt-4.1-2025-04-14"
        )

    def ask_quiz(self, question: str, user_answer: str, answer: str) -> QuizReturn:
        structured_llm = self.with_structured_output(QuizReturn)
        response = structured_llm.invoke(Const.QUIZ_PROMPT.format(
            question=question,
            answer=answer,
            user_answer=user_answer,
            language=Config.LANGUAGE
        ))

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
