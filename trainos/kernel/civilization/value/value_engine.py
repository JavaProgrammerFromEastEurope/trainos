from .value import Value
from .value_type import ValueType


class ValueEngine:

    def determine(self) -> Value:
        return Value(type=ValueType.SURVIVAL)
