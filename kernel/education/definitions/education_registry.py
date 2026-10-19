from kernel.core.registry.base_registry import BaseRegistry

from .education_definition import EducationDefinition


class EducationRegistry(
    BaseRegistry[EducationDefinition],
):
    pass