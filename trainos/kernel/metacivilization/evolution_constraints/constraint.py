from dataclasses import dataclass

from .constraint_type import ConstraintType


@dataclass
class Constraint:

    type: ConstraintType
    immutable: bool