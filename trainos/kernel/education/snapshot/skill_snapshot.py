from dataclasses import dataclass

from kernel.education.skills.skill_level import SkillLevel


@dataclass(frozen=True, slots=True)
class SkillSnapshot:

    skill_id: str
    level: SkillLevel