from dataclasses import dataclass


@dataclass
class QuizReturn:
    correct: bool
    hint: None | str
    percentile: int
    was_missing: None | str
