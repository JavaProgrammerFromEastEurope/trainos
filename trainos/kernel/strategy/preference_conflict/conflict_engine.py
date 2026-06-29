from .conflict_pair import PreferenceConflictPair
from .conflict_resolution import PreferenceResolution


class ConflictEngine:

    def resolve(
        self,
        pair: PreferenceConflictPair
    ) -> PreferenceResolution:
        if pair.left.weight >= pair.right.weight:
            return PreferenceResolution(
                winner=pair.left,
            )
        return PreferenceResolution(winner=pair.right)
