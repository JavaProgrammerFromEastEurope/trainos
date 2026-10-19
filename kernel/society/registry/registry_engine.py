from .citizen_record import CitizenRecord


class RegistryEngine:

    def process(
        self,
        record: CitizenRecord,
    ) -> CitizenRecord:
        return record
