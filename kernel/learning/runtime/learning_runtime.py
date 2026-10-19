class LearningRuntime:

    def __init__(self) -> None:
        self.step_count = 0

    def tick(self) -> int:
        self.step_count += 1
        return self.step_count
