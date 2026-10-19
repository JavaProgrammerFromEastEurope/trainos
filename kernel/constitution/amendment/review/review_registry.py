from __future__ import annotations

from .constitutional_review import ConstitutionalReview


class ReviewRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalReview] = []

    def register(
        self,
        review: ConstitutionalReview,
    ) -> None:
        self._entries.append(review)

    def reviews(self) -> tuple[ConstitutionalReview, ...]:
        return tuple(self._entries)
