from dataclasses import dataclass

from .skill_type import (
    SkillType,
)


@dataclass
class SkillRecord:

    skill: SkillType
