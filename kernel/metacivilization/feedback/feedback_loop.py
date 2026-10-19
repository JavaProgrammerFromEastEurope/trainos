from dataclasses import dataclass


@dataclass
class FeedbackLoop:

    source: 		str
    target: 		str
    strength: float