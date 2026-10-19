from __future__ import annotations

from collections import defaultdict

from .command_snapshot import CommandSnapshot



class CommandSnapshotService:
    """Stores a bounded in-memory history of command snapshots."""

    def __init__(self, max_history_per_command: int = 20) -> None:
        if max_history_per_command < 1:
            raise ValueError("max_history_per_command must be positive")

        self._max_history = max_history_per_command
        self._snapshots: dict[str, list[CommandSnapshot]] = defaultdict(list)

    def capture(
        self,
        *,
        command_id: str,
        command_type: str,
        command_state: str,
        attempt_count: int,
        execution_status: str,
        active_handler: str | None = None,
        error_message: str | None = None,
    ) -> CommandSnapshot:
        """Capture and store a command execution snapshot."""
        snapshot = CommandSnapshot.create(
            command_id=command_id,
            command_type=command_type,
            command_state=command_state,
            attempt_count=attempt_count,
            execution_status=execution_status,
            active_handler=active_handler,
            error_message=error_message,
        )

        history = self._snapshots[command_id]
        history.append(snapshot)

        if len(history) > self._max_history:
            del history[:-self._max_history]

        return snapshot

    def get_latest(self, command_id: str) -> CommandSnapshot | None:
        """Return the most recent snapshot for a command."""
        history = self._snapshots.get(command_id)
        return history[-1] if history else None

    def get_history(
        self,
        command_id: str,
    ) -> tuple[CommandSnapshot, ...]:
        """Return an immutable view of the stored history."""
        return tuple(self._snapshots.get(command_id, ()))

    def clear(self, command_id: str | None = None) -> None:
        """Clear one command's history or all stored snapshots."""
        if command_id is None:
            self._snapshots.clear()
        else:
            self._snapshots.pop(command_id, None)
