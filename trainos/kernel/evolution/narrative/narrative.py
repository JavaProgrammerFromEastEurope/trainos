from dataclasses import dataclass

from .narrative_type import NarrativeType


@dataclass
class Narrative:

    type: NarrativeType
    description: str