from .sensor import Sensor
from .sensor_type import SensorType


class ImuSensor(
    Sensor,
):

    def __init__(self):
        super().__init__(
            SensorType.IMU,
        )
