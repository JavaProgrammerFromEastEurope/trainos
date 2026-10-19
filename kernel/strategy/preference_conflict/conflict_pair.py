from dataclasses import dataclass

from kernel.strategy.preference.preference_weight import PreferenceWeight


@dataclass(frozen=True)
class PreferenceConflictPair:

    left: PreferenceWeight
    right: PreferenceWeight
