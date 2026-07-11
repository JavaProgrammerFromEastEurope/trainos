from dataclasses import dataclass

from kernel.healthcare.runtime.healthcare_lifecycle import HealthcareLifecycle


@dataclass(frozen=True, slots=True)
class HealthcareRuntimeSnapshot:

    lifecycle: HealthcareLifecycle