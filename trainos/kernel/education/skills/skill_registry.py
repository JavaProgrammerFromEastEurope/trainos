from kernel.core.registry.base_registry import BaseRegistry

from .skill import Skill


class SkillRegistry(
    BaseRegistry[Skill],
):
    pass
