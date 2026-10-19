class CurriculumMetrics:

    def __init__(
        self,
    ) -> None:
        self.completed_lessons = 0

    def increment(
        self,
    ) -> None:
        self.completed_lessons += 1
