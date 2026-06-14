from __future__ import annotations

from .component import Component


class ComponentContainer:

    def __init__(self) -> None:

        self._components: dict[
            type,
            Component,
        ] = {}

    def add(
        self,
        component: Component,
    ) -> None:
        self._components[type(component)] = component

    def get(
        self,
        component_type: type,
    ):
        return self._components.get(
            component_type,
        )

    def remove(
        self,
        component_type: type,
    ) -> None:
        self._components.pop(
            component_type,
            None,
        )

    def has(
        self,
        component_type: type,
    ) -> bool:
        return component_type in self._components
