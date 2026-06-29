# tests/kernel_runner/config.py

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StageConfig:
    name: str
    tests: list[str]


STAGES: list[StageConfig] = [
    # #
    # # Stage 1
    # #
    # StageConfig(
    #     name="stage1_kernel_core",
    #     tests=[
    #         "tests/stage1",
    #     ],
    # ),
    # #
    # # Stage 2
    # #
    # StageConfig(
    #     name="stage2_runtime",
    #     tests=[
    #         "tests/stage2",
    #     ],
    # ),
    # #
    # # Stage 3
    # #
    # StageConfig(
    #     name="stage3_reactive",
    #     tests=[
    #         "tests/stage3",
    #     ],
    # ),
    # #
    # # Stage 4
    # #
    # StageConfig(
    #     name="stage4_command_execution",
    #     tests=[
    #         "tests/stage4",
    #     ],
    # ),
    # #
    # # Stage 5
    # #
    # StageConfig(
    #     name="stage5_decision_engine",
    #     tests=[
    #         "tests/stage5",
    #     ],
    # ),
    # #
    # # Stage 6
    # #
    # StageConfig(
    #     name="stage6_environment_test",
    #     tests=[
    #         "tests/stage6",
    #     ],
    # ),
    # #
    # # Stage 7
    # #
    # StageConfig(
    #     name="stage7_cognitive_layer",
    #     tests=[
    #         "tests/stage7",
    #     ],
    # ),
    # #
    # # Stage 8
    # #
    # StageConfig(
    #     name="stage8_self_improving_system",
    #     tests=[
    #         "tests/stage8",
    #     ],
    # ),
    # #
    # # Stage 9
    # #
    # StageConfig(
    #     name="stage9_institution_registry",
    #     tests=[
    #         "tests/stage9",
    #     ],
    # ),
    # #
    # # Stage 10
    # #
    # StageConfig(
    #     name="stage10_civilization_layer",
    #     tests=[
    #         "tests/stage10",
    #     ],
    # ),
    # #
    # # Stage 11
    # #
    # StageConfig(
    #     name="stage11_metacivilization_layer",
    #     tests=[
    #         "tests/stage11",
    #     ],
    # ),
    # #
    # # Stage 12
    # #
    # StageConfig(
    #     name="stage12_recursive_runtime_level",
    #     tests=[
    #         "tests/stage12",
    #     ],
    # ),
    #
    # Stage 14
    #
    StageConfig(
        name="stage14_coverage_level",
        tests=[
            "tests/stage14",
        ],
    ),
]
