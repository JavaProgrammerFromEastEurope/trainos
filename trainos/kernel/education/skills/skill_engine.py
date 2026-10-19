from .skill import Skill
from .skill_level import SkillLevel


class SkillEngine:

    def improve(
        self,
        skill: Skill,
    ) -> Skill:
        progression = {
            SkillLevel.NOVICE: SkillLevel.INTERMEDIATE,
            SkillLevel.INTERMEDIATE: SkillLevel.ADVANCED,
            SkillLevel.ADVANCED: SkillLevel.EXPERT,
            SkillLevel.EXPERT: SkillLevel.EXPERT,
        }
        return Skill(
            skill_id=skill.skill_id,
            student_id=skill.student_id,
            name=skill.name,
            level=progression[skill.level],
        )
