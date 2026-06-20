from trainos.kernel.learning.curriculum.curriculum_engine import (
    CurriculumEngine,
)


def test_curriculum_learning():

    engine 	= CurriculumEngine()
    stage 	= engine.next_stage(level=0)

    assert stage.level == 1
