from __future__ import annotations

from .reflection_result import (
    ReflectionResult,
)


class ReflectionEngine:

    def reflect(
        self,
        success: bool,
    ) -> ReflectionResult:
        if success:
            return ReflectionResult(
                success=True,
                summary="execution_successful",
            )
        return ReflectionResult(
            success=False,
            summary="execution_failed",
        )
