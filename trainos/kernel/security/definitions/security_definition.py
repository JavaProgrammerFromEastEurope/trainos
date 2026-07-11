from dataclasses import dataclass

from .security_category import SecurityCategory
from .security_type import SecurityType


@dataclass(frozen=True, slots=True)
class SecurityDefinition:

    security_id: str
    name: str
    security_type: SecurityType
    category: SecurityCategory