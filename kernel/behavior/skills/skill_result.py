from dataclasses import dataclass

from .skill_status import (
    SkillStatus,
)


@dataclass
class SkillResult:

    status: SkillStatus
    message: str = ""
