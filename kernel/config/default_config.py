# kernel/config/default_config.py

from __future__ import annotations

DEFAULT_CONFIG: dict[str, object] = {
    "simulation.fixed_dt": 0.1,
    "telemetry.max_records": 10000,
    "scheduler.max_queue_size": 100000,
    "event_bus.max_queue_size": 100000,
    "logger.level": "INFO",
    "kernel.shutdown_timeout": 5.0,
}
