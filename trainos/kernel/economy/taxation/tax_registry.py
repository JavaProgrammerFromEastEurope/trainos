from __future__ import annotations

from .tax_definition import TaxDefinition


class TaxRegistry:

    def __init__(self) -> None:
        self._definitions: dict[str, TaxDefinition] = {}

    def register(
        self,
        definition: TaxDefinition,
    ) -> None:
        self._definitions[definition.tax_id] = definition

    def get(
        self,
        tax_id: str,
    ) -> TaxDefinition | None:
        return self._definitions.get(tax_id)

    def all(
        self,
    ) -> tuple[TaxDefinition, ...]:
        return tuple(self._definitions.values())
