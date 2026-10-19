from kernel.core.registry.base_registry import BaseRegistry

from .education_program import EducationProgram


class EducationProgramRegistry(
    BaseRegistry[EducationProgram],
):
    pass
