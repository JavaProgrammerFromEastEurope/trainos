from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StudentPolicy:

    allow_graduation: bool = True
    allow_dropout: 		bool = True