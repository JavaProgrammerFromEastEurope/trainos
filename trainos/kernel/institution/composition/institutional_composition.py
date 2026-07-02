from dataclasses import dataclass

from .composition_relation import CompositionRelation


@dataclass(frozen=True)
class InstitutionalComposition:

    relations: tuple[CompositionRelation, ...]
