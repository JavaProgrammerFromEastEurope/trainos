from __future__ import annotations

from dataclasses import dataclass
from trainos.kernel.state.state_change_record import (
    StateChangeRecord,
)
from trainos.kernel.state.state_history_record import (
    StateHistoryRecord,
)


@dataclass(frozen=True)
class StateSnapshot:

    data: dict[str, object]
    changes: tuple[
        StateChangeRecord,
        ...,
    ] = ()

    history: tuple[
        StateHistoryRecord,
        ...,
    ] = ()
