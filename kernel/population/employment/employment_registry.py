from kernel.core.registry.base_registry import BaseRegistry

from .employment import Employment


class EmploymentRegistry(
    BaseRegistry[Employment],
):
    pass
