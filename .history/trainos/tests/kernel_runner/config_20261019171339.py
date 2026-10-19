# tests/kernel_runner/config.py

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StageConfig:
    name: str
    tests: list[str]


STAGES: list[StageConfig] = [
    /
    #
		# Stage 38
		#
		StageConfig(
				name="stage38_command_layer",
				tests=[
						"tests/stage38",
				],
		),
]
