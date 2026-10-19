from dataclasses import dataclass

from .sensor_reading import SensorReading


@dataclass
class SensorSnapshot:
    readings: tuple[SensorReading, ...]
