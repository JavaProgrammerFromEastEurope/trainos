from dataclasses import dataclass

from .htn_task import (
    HTNTask,
)


@dataclass
class HTNMethod:
    task: HTNTask
