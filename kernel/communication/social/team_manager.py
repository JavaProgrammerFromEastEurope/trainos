from __future__ import annotations

from .team import Team


class TeamManager:

    def __init__(self) -> None:
        self._teams: list[Team] = []

    def add(self, team: Team) -> None:
        self._teams.append(team)

    def teams(self) -> tuple[Team, ...]:
        return tuple(self._teams)
