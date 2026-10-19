from kernel.core.registry.base_registry import BaseRegistry

from .healthcare_snapshot import HealthcareSnapshot


class HealthcareSnapshotRegistry(
    BaseRegistry[HealthcareSnapshot],
):
    pass
