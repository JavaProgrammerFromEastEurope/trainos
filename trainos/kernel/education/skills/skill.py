from dataclasses import dataclass

from .skill_level import SkillLevel


@dataclass(frozen=True, slots=True)
class Skill:

    skill_id: 		str
    student_id: 	str
    name: 				str
    level: SkillLevel