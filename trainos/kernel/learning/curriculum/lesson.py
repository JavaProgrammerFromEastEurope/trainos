from dataclasses import dataclass

from .difficulty_level import DifficultyLevel


@dataclass
class Lesson:

    name: str
    difficulty: DifficultyLevel
