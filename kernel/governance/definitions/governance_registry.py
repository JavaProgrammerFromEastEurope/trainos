from kernel.core.registry.base_registry import BaseRegistry

from .governance_definition import GovernanceDefinition


class GovernanceRegistry(
    BaseRegistry[GovernanceDefinition],
):
    pass
