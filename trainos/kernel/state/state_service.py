from __future__ import annotations

from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)

from trainos.kernel.state.events.state_changed_event import (
    StateChangedEvent,
)

from trainos.kernel.state.state_change_record import (
    StateChangeRecord,
)

from trainos.kernel.state.state_history import (
    StateHistory,
)

from trainos.kernel.state.state_history_record import (
    StateHistoryRecord,
)

from trainos.kernel.state.state_observer import (
    StateObserver,
)

from trainos.kernel.state.state_snapshot import (
    StateSnapshot,
)

from trainos.kernel.state.state_transaction import (
    StateTransaction,
)

from trainos.kernel.state.state_metrics import (
    StateMetrics,
)

from trainos.kernel.state.debug.state_inspector import (
    StateInspector,
)

from trainos.kernel.state.serialization.state_exporter import (
    StateExporter,
)

from trainos.kernel.state.serialization.state_importer import (
    StateImporter,
)

from trainos.kernel.state.control.state_controller import (
    StateController,
)


class StateService(
    KernelService,
):

    def __init__(self) -> None:
        super().__init__(
            name="state",
            dependencies=(),
        )
        self._state: dict[str, object] = {}
        self._changes: list[
            StateChangeRecord
        ] = []
        self._history = StateHistory()
        self._observers: list[
            StateObserver
        ] = []
        self._metrics 	= StateMetrics()
        self._inspector = StateInspector(self)
        self._exporter 	= StateExporter()
        self._importer 	= StateImporter()
        self._controller = StateController(self)
        self._tick = 0

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(
            ServiceState.INITIALIZED,
        )

    def start(self) -> None:
        self._set_state(
            ServiceState.RUNNING,
        )

    def stop(self) -> None:
        self._set_state(
            ServiceState.STOPPED,
        )

    def dispose(self) -> None:
        self._state.clear()
        self._changes.clear()
        self._history.clear()
        self._observers.clear()

    def update(self, dt: float) -> None:
        self._tick += 1
        self._metrics.tick_count 		= self._tick
        self._metrics.key_count 		= len(self._state)
        self._metrics.change_count 	= len(self._changes)
        self._metrics.watcher_count = len(self._observers)
        self._metrics.history_size 	= self._history.size

    def inspector(self) -> StateInspector:
        return self._inspector

    def exporter(self) -> StateExporter:
        return self._exporter

    def importer(self) -> StateImporter:
        return self._importer

    def controller(self) -> StateController:
        return self._controller

    def transaction(self) -> StateTransaction:
        return StateTransaction(self)

    def watch(self, key, callback) -> None:
        self._observers.append(
            StateObserver(key, callback)
        )

    def unwatch(self, callback) -> None:
        self._observers = [
            o for o in self._observers
            if o.callback != callback
        ]

    def _notify(self, key, old_value, new_value) -> None:
        for observer in self._observers:
            if observer.key != key:
                continue
            observer.callback(
                key,
                old_value,
                new_value,
            )

    def set(self, key, value) -> None:
        if self._controller.is_paused():
            return
        old_value = self._state.get(key)
        self._state[key] = value
        self._changes.append(
            StateChangeRecord(
                key,
                old_value,
                value,
            )
        )
        self._history.append(
            StateHistoryRecord(
                self._tick,
                key,
                old_value,
                value,
            )
        )
        self._notify(
            key,
            old_value,
            value,
        )
        if self._kernel is not None:
            self._kernel.publish(
                StateChangedEvent(
                    key,
                    old_value,
                    value,
                )
            )

    def get(self, key, default=None):
        return self._state.get(key, default)

    def has(self, key) -> bool:
        return key in self._state

    def remove(self, key) -> None:
        if key not in self._state:
            return
        old_value = self._state[key]
        del self._state[key]
        self._changes.append(
            StateChangeRecord(
                key,
                old_value,
                None,
            )
        )
        self._history.append(
            StateHistoryRecord(
                self._tick,
                key,
                old_value,
                None,
            )
        )
        self._notify(
            key,
            old_value,
            None,
        )
        if self._kernel is not None:
            self._kernel.publish(
                StateChangedEvent(
                    key,
                    old_value,
                    None,
                )
            )

    def clear(self) -> None:
        self._state.clear()
        self._changes.clear()
        self._history.clear()

    @property
    def metrics(self) -> StateMetrics:
        return self._metrics

    @property
    def changes(self):
        return tuple(self._changes)

    @property
    def history(self) -> StateHistory:
        return self._history

    def snapshot(self) -> StateSnapshot:
        return StateSnapshot(
            data=dict(self._state),
            changes=tuple(self._changes),
            history=self._history.records,
        )

    def health_check(self) -> bool:
        return True
