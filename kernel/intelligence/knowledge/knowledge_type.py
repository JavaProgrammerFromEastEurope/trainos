from enum import Enum


class KnowledgeType(Enum):

    FACT 		= "fact"
    RULE 		= "rule"
    OBSERVATION = "observation"
    THEORY 	= "theory"
    HISTORY = "history"