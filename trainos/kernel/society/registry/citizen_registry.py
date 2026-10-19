from ...core.registry.base_registry import BaseRegistry

from .citizen_record import CitizenRecord


class CitizenRegistry(BaseRegistry[CitizenRecord]):

    def register_citizen(
        self,
        record: CitizenRecord,
    ) -> None:
        self.register(record.entity_id, record)
