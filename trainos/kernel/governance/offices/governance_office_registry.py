from kernel.core.registry.base_registry import BaseRegistry

from .governance_office import GovernanceOffice


class GovernanceOfficeRegistry(
    BaseRegistry[GovernanceOffice],
):
    pass
