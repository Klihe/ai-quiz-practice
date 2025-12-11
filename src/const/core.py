class Const:
    QUIZ_PROMPT: str = """
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

        Language: {language}
    """
