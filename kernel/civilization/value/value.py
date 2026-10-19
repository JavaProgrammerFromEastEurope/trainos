from dataclasses import dataclass

from .value_type import ValueType


@dataclass
class Value:

    type: ValueType
