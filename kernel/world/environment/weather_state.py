from dataclasses import dataclass

from .weather_type import WeatherType


@dataclass
class WeatherState:
    weather: WeatherType
