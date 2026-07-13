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
    # #
    # # Stage 13
    # #
    # StageConfig(
    #     name="stage13_some_level",
    #     tests=[
    #         "tests/stage13",
    #     ],
    # ),
    # #
    # # Stage 14
    # #
    # StageConfig(
    #     name="stage14_coverage_level",
    #     tests=[
    #         "tests/stage14",
    #     ],
    # ),
    # #
    # # Stage 15
    # #
    # StageConfig(
    #     name="stage15_Arbitration_level",
    #     tests=[
    #         "tests/stage15",
    #     ],
    # ),
    # #
    # # Stage 16
    # #
    # StageConfig(
    #     name="stage16_Principles_level",
    #     tests=[
    #         "tests/stage16",
    #     ],
    # ),
    # #
    # # Stage 17
    # #
    # StageConfig(
    #     name="stage17_constitutional_level",
    #     tests=[
    #         "tests/stage17",
    #     ],
    # ),
    # #
    # # Stage 18
    # #
    # StageConfig(
    #     name="stage18_constitutional_audit_level",
    #     tests=[
    #         "tests/stage18",
    #     ],
    # ),
    # #
    # # Stage 19
    # #
    # StageConfig(
    #     name="stage19_institutional_level",
    #     tests=[
    #         "tests/stage19",
    #     ],
    # ),
    # #
    # # Stage 20
    # #
    # StageConfig(
    #     name="stage20_citizen_level",
    #     tests=[
    #         "tests/stage20",
    #     ],
    # ),
    # #
    # # Stage 21
    # #
    # StageConfig(
    #     name="stage21_budget_level",
    #     tests=[
    #         "tests/stage21",
    #     ],
    # ),
    # #
    # # Stage 22
    # #
    # StageConfig(
    #     name="stage22_inventory_engine_level",
    #     tests=[
    #         "tests/stage22",
    #     ],
    # ),
    # #
    # # Stage 23
    # #
    # StageConfig(
    #     name="stage23_production_job_level",
    #     tests=[
    #         "tests/stage23",
    #     ],
    # ),
    # #
    # # Stage 24
    # #
    # StageConfig(
    #     name="stage24_logistics_level",
    #     tests=[
    #         "tests/stage24",
    #     ],
    # ),
    # #
    # # Stage 25
    # #
    # StageConfig(
    #     name="stage25_consumption_snapshot_level",
    #     tests=[
    #         "tests/stage25",
    #     ],
    # ),
    # #
    # # Stage 26
    # #
    # StageConfig(
    #     name="stage26_population_definition_level",
    #     tests=[
    #         "tests/stage26",
    #     ],
    # ),
    # #
    # # Stage 27
    # #
    # StageConfig(
    #     name="stage27_healthcare_level",
    #     tests=[
    #         "tests/stage27",
    #     ],
    # ),
    # #
    # # Stage 28
    # #
    # StageConfig(
    #     name="stage28_educational_level",
    #     tests=[
    #         "tests/stage28",
    #     ],
    # ),
    # #
    # # Stage 29
    # #
    # StageConfig(
    #     name="stage29_security_level",
    #     tests=[
    #         "tests/stage29",
    #     ],
    # ),
    # #
    # # Stage 30
    # #
    # StageConfig(
    #     name="stage30_governance_level",
    #     tests=[
    #         "tests/stage30",
    #     ],
    # ),
    # #
    # # Stage 31
    # #
    # StageConfig(
    #     name="stage31_simulation_level",
    #     tests=[
    #         "tests/stage31",
    #     ],
    # ),
    # #
    # # Stage 32
    # #
    # StageConfig(
    #     name="stage32_integration_level",
    #     tests=[
    #         "tests/stage32",
    #     ],
    # ),
    # #
    # # Stage 33
    # #
    # StageConfig(
    #     name="stage33_persistence_level",
    #     tests=[
    #         "tests/stage33",
    #     ],
    # ),
    # #
    # # Stage 34
    # #
    # StageConfig(
    #     name="stage34_configuration_layer",
    #     tests=[
    #         "tests/stage34",
    #     ],
    # ),
    #
    # Stage 35
    #
    StageConfig(
        name="stage35_scheduling_layer",
        tests=[
            "tests/stage35",
        ],
    ),
]
