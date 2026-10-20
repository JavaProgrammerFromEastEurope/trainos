from enum import Enum


class CommandEventType(Enum):
    COMMAND_CREATED = "command_created"
    COMMAND_STARTED = "command_started"
    COMMAND_PROGRESS_UPDATED = "command_progress_updated"
    COMMAND_RETRYING = "command_retrying"
    COMMAND_COMPLETED = "command_completed"
    COMMAND_FAILED = "command_failed"
    COMMAND_CANCELLED = "command_cancelled"
    EXECUTION_INTEGRITY_DIAGNOSTIC = "execution_integrity_diagnostic"
