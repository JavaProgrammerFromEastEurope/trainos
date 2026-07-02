from enum import Enum


class RuleType(Enum):

    IMMUTABLE 	= "immutable"
    MODIFIABLE 	= "modifiable"
    CONDITIONAL = "conditional"