from __future__ import annotations

from .skill import (
    Skill,
)

from .skill_type import (
    SkillType,
)


class SkillRegistry:

    def __init__(
        self,
    ) -> None:
        self._skills: dict[
            SkillType,
            Skill,
        ] = {}

    def register(
        self,
        skill_type: SkillType,
        skill: Skill,
    ) -> None:
        self._skills[skill_type] = skill

    def get(
        self,
        skill_type: SkillType,
    ) -> Skill | None:
        return self._skills.get(
            skill_type,
        )
