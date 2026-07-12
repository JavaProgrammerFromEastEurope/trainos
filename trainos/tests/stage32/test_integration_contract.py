from kernel.integration.contracts.integration_contract import IntegrationContract
from kernel.integration.contracts.contract_type import ContractType


def test_integration_contract():

    contract = IntegrationContract(
        contract_id="CONTRACT1",
        contract_type=ContractType.POPULATION,
        name="ResidentCreated",
    )

    assert contract.contract_id == "CONTRACT1"
    assert contract.contract_type == ContractType.POPULATION
    assert contract.name == "ResidentCreated"
