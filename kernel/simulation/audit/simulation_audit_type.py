from enum import Enum


class SimulationAuditType(Enum):

    TICK_EXECUTED 	= "tick_executed"
    EVENT_PROCESSED = "event_processed"
    RUNTIME_CHANGED = "runtime_changed"
    ERROR_OCCURRED 	= "error_occurred"