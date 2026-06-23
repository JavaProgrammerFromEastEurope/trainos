from trainos.kernel.metacivilization.interaction.interaction_matrix import (
    InteractionMatrix,
)
from trainos.kernel.metacivilization.interaction.system_link import SystemLink


def test_interaction_matrix_add_link():

    matrix = InteractionMatrix()

    link = SystemLink(
        source="goals",
        target="ethics",
        weight=1.0,
    )

    matrix.add_link(link)

    assert matrix.links() == (link,)
