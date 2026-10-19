from dataclasses import dataclass


@dataclass(frozen=True)
class CompositionRelation:

    container_id: str
    component_id: str