from kernel.core.registry.base_registry import BaseRegistry

from .healthcare_history_entry import HealthcareHistoryEntry


class HealthcareHistoryRegistry(
    BaseRegistry[HealthcareHistoryEntry],
):
    pass
