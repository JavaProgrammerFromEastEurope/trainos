from trainos.kernel.metacivilization.evolution_constraints.constraint_engine import ConstraintEngine
from trainos.kernel.metacivilization.evolution_constraints.constraint import Constraint
from trainos.kernel.metacivilization.evolution_constraints.constraint_type import ConstraintType


def test_constraint_engine_validate():

    engine = ConstraintEngine()
    constraint = Constraint(
        type=ConstraintType.SURVIVAL,
        immutable=True,
    )

    assert engine.validate(constraint) is True