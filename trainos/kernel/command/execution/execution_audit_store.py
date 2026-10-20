from __future__ import annotations

import sqlite3
from pathlib import Path
from threading import RLock
from typing import Any

from .command_execution import CommandExecution


class ExecutionAuditStore:
    """Append-only SQLite history of execution state transitions.

    Each save appends a transition record rather than overwriting the previous
    state. The database can be reopened after process restart to inspect history.
    This is an application audit log, not a tamper-proof safety log.
    """

    def __init__(self, database_path: str | Path) -> None:
        if not isinstance(database_path, (str, Path)) or not str(database_path).strip():
            raise ValueError("database_path must not be empty")
        self._database_path = str(database_path)
        self._lock = RLock()
        self._connection = sqlite3.connect(self._database_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        with self._lock, self._connection:
            self._connection.execute("PRAGMA foreign_keys = ON")
            self._connection.execute(
                """CREATE TABLE IF NOT EXISTS execution_audit (
                    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                    execution_id TEXT NOT NULL,
                    command_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    attempts INTEGER NOT NULL,
                    max_attempts INTEGER NOT NULL,
                    completed INTEGER NOT NULL,
                    recorded_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                    UNIQUE(execution_id, status)
                )"""
            )
            self._connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_execution_audit_command ON execution_audit(command_id, sequence)"
            )

    @property
    def database_path(self) -> str:
        return self._database_path

    def append(self, execution: CommandExecution) -> None:
        """Persist a state transition once; duplicate same-state writes are idempotent."""
        if not isinstance(execution, CommandExecution):
            raise TypeError("execution must be a CommandExecution")
        with self._lock, self._connection:
            existing = self._connection.execute(
                "SELECT command_id, attempts, max_attempts, completed FROM execution_audit "
                "WHERE execution_id = ? AND status = ?",
                (execution.execution_id, execution.status.value),
            ).fetchone()
            values = (
                execution.command_id,
                execution.progress.attempts,
                execution.progress.max_attempts,
                int(execution.progress.completed),
            )
            if existing is not None:
                if tuple(existing) != values:
                    raise ValueError("conflicting duplicate execution state")
                return
            latest = self._connection.execute(
                "SELECT command_id, status FROM execution_audit WHERE execution_id = ? "
                "ORDER BY sequence DESC LIMIT 1",
                (execution.execution_id,),
            ).fetchone()
            if latest is None:
                if execution.status.value != "created":
                    raise ValueError("first execution audit state must be created")
            else:
                if latest["command_id"] != execution.command_id:
                    raise ValueError("execution_id cannot be reused for another command")
                allowed_next = {
                    "created": {"running", "failed"},
                    "running": {"completed", "failed"},
                    "completed": set(),
                    "failed": set(),
                }
                if execution.status.value not in allowed_next[latest["status"]]:
                    raise ValueError(
                        f"invalid execution audit transition: {latest['status']} -> {execution.status.value}"
                    )
            self._connection.execute(
                "INSERT INTO execution_audit "
                "(execution_id, command_id, status, attempts, max_attempts, completed) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (execution.execution_id, execution.command_id, execution.status.value, *values[1:]),
            )

    def get_history(self, execution_id: str) -> tuple[dict[str, Any], ...]:
        if not isinstance(execution_id, str) or not execution_id.strip():
            raise ValueError("execution_id must not be empty")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, execution_id, command_id, status, attempts, max_attempts, "
                "completed, recorded_at FROM execution_audit WHERE execution_id = ? ORDER BY sequence",
                (execution_id,),
            ).fetchall()
        return tuple(dict(row) for row in rows)

    def get_command_history(self, command_id: str) -> tuple[dict[str, Any], ...]:
        if not isinstance(command_id, str) or not command_id.strip():
            raise ValueError("command_id must not be empty")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, execution_id, command_id, status, attempts, max_attempts, "
                "completed, recorded_at FROM execution_audit WHERE command_id = ? ORDER BY sequence",
                (command_id,),
            ).fetchall()
        return tuple(dict(row) for row in rows)

    def close(self) -> None:
        with self._lock:
            self._connection.close()

    def __enter__(self) -> "ExecutionAuditStore":
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self.close()
