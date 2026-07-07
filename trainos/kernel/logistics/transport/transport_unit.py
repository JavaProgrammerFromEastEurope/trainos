from dataclasses import dataclass

from .transport_status import TransportStatus
from .transport_type import TransportType


@dataclass(frozen=True, slots=True)
class TransportUnit:

    transport_id: 	str
    name: 					str
    transport_type: TransportType
    status: TransportStatus