from dataclasses import dataclass

from .preference_weight import PreferenceWeight


@dataclass(frozen=True)
class PreferenceProfile:

    weights: tuple[PreferenceWeight, ...]
