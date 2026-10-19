from dataclasses import dataclass


@dataclass
class MetaState:

    reflection: 		object | None = None
    self_awareness: object | None = None
    goals: 					object | None = None
    planning: 			object | None = None
    meaning: 				object | None = None
    destiny: 				object | None = None
    risk: 					object | None = None
    ethics: 				object | None = None