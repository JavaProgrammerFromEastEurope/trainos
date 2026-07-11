from kernel.core.registry.base_registry import BaseRegistry

from .medical_condition import MedicalCondition


class MedicalConditionRegistry(
    BaseRegistry[MedicalCondition],
):
    pass
