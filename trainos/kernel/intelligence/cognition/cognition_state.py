from dataclasses import dataclass


@dataclass(frozen=True)
class CognitionState:

    awareness_level: 	float
    coherence: 				float
