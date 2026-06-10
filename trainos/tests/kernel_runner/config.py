from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class StageConfig:
    name: str
    tests: List[str]


STAGES = [
    StageConfig(
        name="stage1_kernel_core",
        tests=[
            "tests/stage1/test_kernel_bootstrap.py",
            "tests/stage1/test_service_registry.py",
            "tests/stage1/test_service_lifecycle.py",
        ],
    ),
    StageConfig(
        name="stage1_event_system",
        tests=[
            "tests/stage1/test_event_bus_basic.py",
            "tests/stage1/test_event_bus_multiple_subscribers.py",
            "tests/stage1/test_event_ordering.py",
        ],
    ),
    StageConfig(
        name="stage1_stability",
        tests=[
            "tests/stage1/test_tick_loop.py",
            "tests/stage1/test_event_queue_stability.py",
            "tests/stage1/test_kernel_reentrancy.py",
        ],
    ),
]
