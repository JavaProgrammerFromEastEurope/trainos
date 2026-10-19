from __future__ import annotations

from .environment_state import EnvironmentState
from .weather_state import WeatherState
from .weather_type import WeatherType
from .temperature_state import TemperatureState
from .wind_state import WindState
from .light_state import LightState
from .noise_state import NoiseState


class EnvironmentService:

    def __init__(
        self,
    ) -> None:
        self._state = EnvironmentState(
            weather=WeatherState(
                WeatherType.CLEAR,
            ),
            temperature=TemperatureState(),
            wind=WindState(),
            light=LightState(),
            noise=NoiseState(),
        )

    @property
    def state(
        self,
    ) -> EnvironmentState:
        return self._state
