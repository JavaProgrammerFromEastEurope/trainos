from dataclasses 	import dataclass
from .base_goal 	import GovernorGoal


@dataclass(slots=True)
class RepairGeneratorGoal(GovernorGoal):

    sector_id: 		int
    generator_id: int
    damage: 			float

    def generate_tasks(self):
        return [
            {
                "type": "INSPECT_GENERATOR",
                "generator_id": self.generator_id,
            },
            {
                "type": "REPLACE_MEMBRANE",
                "generator_id": self.generator_id,
            },
            {
                "type": "RESTART_GENERATOR",
                "generator_id": self.generator_id,
            },
        ]