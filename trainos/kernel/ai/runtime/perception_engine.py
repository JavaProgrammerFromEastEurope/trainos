from __future__ import annotations

from trainos.kernel.state.state_service import (
    StateService,
)

from .perception_result import (
    PerceptionResult,
)


class PerceptionEngine:

    def perceive(
        self,
        state_service: StateService,
    ) -> PerceptionResult:
        return PerceptionResult(
            observations=state_service.snapshot().data,
        )
