from __future__ import annotations

from .learning_session import LearningSession


class SessionHistory:

    def __init__(
        self,
    ) -> None:
        self._sessions: list[LearningSession] = []

    def add(
        self,
        session: LearningSession,
    ) -> None:
        self._sessions.append(session)

    def sessions(
        sdelf,
    ) -> tuple[LearningSession, ...]:
        return tuple(self._sessions)
