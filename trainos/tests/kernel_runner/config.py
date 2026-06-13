# tests/kernel_runner/config.py

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StageConfig:
    name: str
    tests: list[str]


STAGES: list[StageConfig] = [
    #
    # Stage 1
    #
    StageConfig(
        name="stage1_kernel_core",
        tests=[
            "tests/stage1",
        ],
    ),
    #
    # Stage 2
    #
    StageConfig(
        name="stage2_runtime",
        tests=[
            "tests/stage2",
        ],
    ),
    #
    # Stage 3
    #
    StageConfig(
        name="stage3_reactive",
        tests=[
            "tests/stage3",
        ],
    ),
]
