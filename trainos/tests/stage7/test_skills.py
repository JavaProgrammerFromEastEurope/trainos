from kernel.behavior.skills.skill import (
    Skill,
)

from kernel.behavior.skills.skill_context import SkillContext
from kernel.behavior.skills.skill_status import SkillStatus


def test_skills():

    skill = Skill()
    result = skill.execute(SkillContext())

    assert result.status == SkillStatus.SUCCESS
