from __future__ import annotations

from .skill import (
    Skill,
)

from .skill_context import (
    SkillContext,
)

from .skill_result import (
    SkillResult,
)


class SkillExecutor:

    def execute(
        self,
        skill: Skill,
        context: SkillContext,
    ) -> SkillResult:
        return skill.execute(
            context,
        )
