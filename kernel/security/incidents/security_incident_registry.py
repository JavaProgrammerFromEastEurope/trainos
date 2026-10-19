from kernel.core.registry.base_registry import BaseRegistry

from .security_incident import SecurityIncident


class SecurityIncidentRegistry(
    BaseRegistry[SecurityIncident],
):
    pass
