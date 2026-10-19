from dataclasses import dataclass

from kernel.logistics.transport.transport_status import TransportStatus


@dataclass(frozen=True, slots=True)
class LogisticsTransportSnapshot:

    transport_id: str
    status: TransportStatus