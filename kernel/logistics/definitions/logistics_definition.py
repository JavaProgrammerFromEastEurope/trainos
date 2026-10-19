from dataclasses import dataclass

from .logistics_category 	import LogisticsCategory
from .logistics_type 			import LogisticsType


@dataclass(frozen=True, slots=True)
class LogisticsDefinition:

    logistics_id: str
    name: str
    logistics_type: LogisticsType
    category: LogisticsCategory