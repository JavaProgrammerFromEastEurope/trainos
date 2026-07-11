from kernel.education.skills.skill import Skill
from kernel.education.skills.skill_engine import SkillEngine
from kernel.education.skills.skill_level import SkillLevel


def test_skill_engine():

    engine = SkillEngine()
    skill = Skill(
        skill_id="SK1",
        student_id="S1",
        name="Mechanics",
        level=SkillLevel.NOVICE,
    )
    improved = engine.improve(skill)
    assert improved.level == SkillLevel.INTERMEDIATE