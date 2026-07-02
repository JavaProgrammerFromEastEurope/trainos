from trainos.kernel.constitution.conflict.constitutional_conflict import ConstitutionalConflict
from trainos.kernel.constitution.conflict.conflict_engine import ConstitutionalConflictEngine


def test_constitution_conflict_resolution():

    conflict = ConstitutionalConflict(
        left_article="Freedom",
        right_article="Emergency",
    )

    engine = ConstitutionalConflictEngine()
    resolution = engine.resolve(conflict)

    assert resolution.winning_article == "Freedom"