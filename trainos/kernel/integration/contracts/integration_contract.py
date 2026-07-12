from dataclasses import dataclass

from .contract_type import ContractType


@dataclass(frozen=True, slots=True)
class IntegrationContract:

    contract_id: 	str
    contract_type: ContractType
    name: 				str