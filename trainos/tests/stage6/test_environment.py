from trainos.kernel.world.environment.environment_service import (
    EnvironmentService,
)

from trainos.kernel.world.environment.weather_type import (
    WeatherType,
)


def test_environment():

    service = EnvironmentService()

    assert service.state is not None

    assert service.state.weather.weather == WeatherType.CLEAR

    assert service.state.temperature is not None

    assert service.state.wind is not None

    assert service.state.light is not None

    assert service.state.noise is not None
