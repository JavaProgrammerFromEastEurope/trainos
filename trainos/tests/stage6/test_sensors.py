from trainos.kernel.world.sensors.sensor_registry import SensorRegistry
from trainos.kernel.world.sensors.vision_sensor import VisionSensor


def test_sensors():

    registry = SensorRegistry()

    sensor = VisionSensor()

    registry.register(sensor)

    sensors = registry.sensors()

    assert len(sensors) == 1
    assert sensors[0] is sensor
