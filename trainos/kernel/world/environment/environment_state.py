from dataclasses import dataclass

from .weather_state import WeatherState
from .temperature_state import TemperatureState
from .wind_state import WindState
from .light_state import LightState
from .noise_state import NoiseState


@dataclass
class EnvironmentState:

    weather: WeatherState
    temperature: TemperatureState
    wind: WindState
    light: LightState
    noise: NoiseState
