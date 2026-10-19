from .civilization 				import Civilization
from .civilization_state 	import CivilizationState


class CivilizationEngine:

    def run(self) -> Civilization:
        return Civilization(
            state=CivilizationState.STABLE,
        )
