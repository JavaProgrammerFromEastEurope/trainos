from dataclasses import dataclass

from .preference_dimension import PreferenceDimension


@dataclass(frozen=True)
class PreferenceWeight:

    dimension: PreferenceDimension
    weight: float
