from .sensor import Sensor
from .sensor_type import SensorType


class GpsSensor(
    Sensor,
):

    def __init__(self):
        super().__init__(
            SensorType.GPS,
        )
