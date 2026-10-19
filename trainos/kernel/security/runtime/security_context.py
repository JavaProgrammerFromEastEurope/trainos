from dataclasses import dataclass

from .security_configuration import SecurityConfiguration


@dataclass(slots=True)
class SecurityContext:

    configuration: SecurityConfiguration