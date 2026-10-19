from .transport_status import TransportStatus
from .transport_unit import TransportUnit


class TransportEngine:

    def dispatch(
        self,
        unit: TransportUnit,
    ) -> TransportUnit:
        return TransportUnit(
            transport_id=unit.transport_id,
            name=unit.name,
            transport_type=unit.transport_type,
            status=TransportStatus.BUSY,
        )

    def release(
        self,
        unit: TransportUnit,
    ) -> TransportUnit:
        return TransportUnit(
            transport_id=unit.transport_id,
            name=unit.name,
            transport_type=unit.transport_type,
            status=TransportStatus.AVAILABLE,
        )
