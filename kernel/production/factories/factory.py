from dataclasses import dataclass

from .factory_type 		import FactoryType
from .factory_status	import FactoryStatus


@dataclass(frozen=True, slots=True)
class Factory:

    factory_id: str
    name: 			str
    factory_type: FactoryType
    status: FactoryStatus