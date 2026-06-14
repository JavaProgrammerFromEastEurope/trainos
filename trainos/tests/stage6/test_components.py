from trainos.kernel.world.components.component_container import (
    ComponentContainer,
)

from trainos.kernel.world.components.health_component import (
    HealthComponent,
)


def test_components():

    container = ComponentContainer()
    component = HealthComponent()

    container.add(component)

    assert container.has(HealthComponent) is True

    assert container.get(HealthComponent) is component

    container.remove(HealthComponent)

    assert container.has(HealthComponent) is False
