from kernel.core.registry.base_registry import BaseRegistry

from .student import Student


class StudentRegistry(
    BaseRegistry[Student],
):
    pass
