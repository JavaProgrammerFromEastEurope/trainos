from .curriculum_stage import CurriculumStage


class CurriculumEngine:

    def next_stage(self, level: int) -> CurriculumStage:
        return CurriculumStage(level=level + 1)
