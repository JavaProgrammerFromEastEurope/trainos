from __future__ import annotations

from .amendment_proposal import AmendmentProposal


class AmendmentRegistry:

    def __init__(self) -> None:
        self._entries: list[AmendmentProposal] = []

    def register(self, proposal: AmendmentProposal) -> None:
        self._entries.append(proposal)

    def proposals(self) -> tuple[AmendmentProposal, ...]:
        return tuple(self._entries)
