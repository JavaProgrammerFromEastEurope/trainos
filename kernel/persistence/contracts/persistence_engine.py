from .persistence_contract import PersistenceContract


class PersistenceEngine:

    def prepare(
        self,
        contract: PersistenceContract,
    ) -> PersistenceContract:
        return contract
