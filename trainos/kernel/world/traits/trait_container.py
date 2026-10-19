from __future__ import annotations

from .trait import Trait


class TraitContainer:

    def __init__(
        self,
    ) -> None:
        self._traits: dict[
            type,
            Trait,
        ] = {}

    def add(
        self,
        trait: Trait,
    ) -> None:
        self._traits[type(trait)] = trait

    def get(
        self,
        trait_type: type,
    ):
        return self._traits.get(
            trait_type,
        )

    def remove(
        self,
        trait_type: type,
    ) -> None:
        self._traits.pop(
            trait_type,
            None,
        )

    def has(
        self,
        trait_type: type,
    ) -> bool:
        return trait_type in self._traits
