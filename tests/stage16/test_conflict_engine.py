from kernel.identity.principles.conflict.conflict_engine import PrincipleConflictEngine
from kernel.identity.principles.conflict.principle_conflict import PrincipleConflict
from kernel.identity.principles.civilization_principle import CivilizationPrinciple


def test_conflict_engine():
    engine = PrincipleConflictEngine()

    p1 = CivilizationPrinciple("A", "desc", "absolute")
    p2 = CivilizationPrinciple("B", "desc", "strategic")

    conflict = PrincipleConflict(left=p1, right=p2)

    result = engine.resolve(conflict)

    assert result.winner == p1