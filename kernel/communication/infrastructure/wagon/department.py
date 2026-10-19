from dataclasses import dataclass

from .department_type import DepartmentType


@dataclass
class Department:
    type: DepartmentType
