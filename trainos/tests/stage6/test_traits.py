from trainos.kernel.world.traits.trait_container import (
    TraitContainer,
)

from trainos.kernel.world.traits.movable_trait import (
    MovableTrait,
)


def test_traits():

    container = TraitContainer()

    trait = MovableTrait()

    container.add(trait)

    assert container.has(MovableTrait) is True

    assert container.get(MovableTrait) is trait

    container.remove(MovableTrait)

    assert container.has(MovableTrait) is False

    assert container.get(MovableTrait) is None
