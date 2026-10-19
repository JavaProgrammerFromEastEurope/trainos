from dataclasses import dataclass


@dataclass
class ReasoningMessage:

    source: 	str
    target: 	str
    content: 	str