from __future__ import annotations

from .skill_context import (
    SkillContext,
)

from .skill_result import (
    SkillResult,
)

from .skill_status import (
    SkillStatus,
)


class Skill:

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:
        return SkillResult(
            status=SkillStatus.SUCCESS,
        )
