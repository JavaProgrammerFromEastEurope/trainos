from .sensor import Sensor
from .sensor_type import SensorType


class VisionSensor(
    Sensor,
):
    def __init__(self):
        super().__init__(
            SensorType.VISION,
        )
