from .review_engine import ReviewEngine


class ReviewRuntime:

    def __init__(self) -> None:
        self._engine = ReviewEngine()

    def initialize(self) -> None:
        pass

    def update(self, review):
        return self._engine.review(review)

    def shutdown(self) -> None:
        pass
