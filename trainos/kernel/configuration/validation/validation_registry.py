from kernel.core.registry.base_registry import BaseRegistry

from .validation_rule import ValidationRule


class ValidationRegistry(
    BaseRegistry[ValidationRule],
):
    pass
