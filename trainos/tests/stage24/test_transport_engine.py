from kernel.logistics.transport.transport_engine 	import TransportEngine
from kernel.logistics.transport.transport_status 	import TransportStatus
from kernel.logistics.transport.transport_type 		import TransportType
from kernel.logistics.transport.transport_unit 		import TransportUnit


def test_transport_engine():

    engine = TransportEngine()
    unit = TransportUnit(
        transport_id="TR1",
        name="Cart #1",
        transport_type=TransportType.CART,
        status=TransportStatus.AVAILABLE,
    )

    busy = engine.dispatch(unit)
    assert busy.status == TransportStatus.BUSY

    free = engine.release(busy)
    assert free.status == TransportStatus.AVAILABLE
