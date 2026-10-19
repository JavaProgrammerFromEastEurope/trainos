from __future__ import annotations

from dataclasses import dataclass
from .sensor_type import SensorType


@dataclass
class Sensor:
    type: SensorType
