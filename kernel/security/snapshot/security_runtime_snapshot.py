from dataclasses import dataclass

from kernel.security.runtime.security_lifecycle import SecurityLifecycle


@dataclass(frozen=True, slots=True)
class SecurityRuntimeSnapshot:

    lifecycle: SecurityLifecycle
