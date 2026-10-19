from kernel.core.registry.base_registry import BaseRegistry

from .education_history_entry import EducationHistoryEntry


class EducationHistoryRegistry(
    BaseRegistry[EducationHistoryEntry],
):
    pass