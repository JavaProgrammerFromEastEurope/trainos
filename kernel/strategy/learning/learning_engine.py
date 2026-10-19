from .learning_event import LearningEvent


class LearningEngine:

    def process(
        self,
        event: LearningEvent,
    ) -> LearningEvent:
        return event
