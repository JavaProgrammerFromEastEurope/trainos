from __future__ import annotations

from copy import deepcopy


class StateTransaction:

    def __init__(
        self,
        state_service,
    ) -> None:
        self._state_service = state_service
        self._snapshot = deepcopy(
            state_service._state,
        )
        self._committed = False

    def commit(self) -> None:
        self._committed = True

    def rollback(self) -> None:
        self._state_service._state = deepcopy(
            self._snapshot,
        )

    def __enter__(
        self,
    ):
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> bool:
        if exc_type is not None:
            self.rollback()
            return False
        if not self._committed:
            self.commit()
        return False
