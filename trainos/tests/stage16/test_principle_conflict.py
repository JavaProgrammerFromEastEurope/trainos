from trainos.kernel.identity.principles.conflict.principle_conflict import PrincipleConflict
from trainos.kernel.identity.principles.civilization_principle import CivilizationPrinciple


def test_principle_conflict():
    p1 = CivilizationPrinciple("Protect passengers", "A", "absolute")
    p2 = CivilizationPrinciple("Protect system", "B", "strategic")

    conflict = PrincipleConflict(left=p1, right=p2)

    assert conflict.left.name == "Protect passengers"