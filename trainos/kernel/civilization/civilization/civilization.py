from dataclasses import dataclass

from .civilization_state import CivilizationState


@dataclass
class Civilization:

    state: CivilizationState