from kernel.core.registry.base_registry import BaseRegistry

from .patient import Patient


class PatientRegistry(
    BaseRegistry[Patient],
):
    pass
