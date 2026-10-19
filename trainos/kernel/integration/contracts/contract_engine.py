from .integration_contract import IntegrationContract


class ContractEngine:

    def publish(
        self,
        contract: IntegrationContract,
    ) -> IntegrationContract:
        return contract
