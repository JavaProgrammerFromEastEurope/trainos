from dataclasses import dataclass


@dataclass
class FeedbackEvent:

    origin: 		str
    signal: 		str
    intensity: float