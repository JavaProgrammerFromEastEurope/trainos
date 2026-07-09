from dataclasses import dataclass

from .consumer_status import ConsumerStatus
from .consumer_type 	import ConsumerType


@dataclass(frozen=True, slots=True)
class Consumer:

    consumer_id:	str
    name: 				str
    consumer_type: ConsumerType
    status: ConsumerStatus