from trainos.modules.drone.drone_entity import DroneEntity


class DroneCommands:

    @staticmethod
    def move(drone: DroneEntity, dx: float, dy: float):

        drone.x += dx
        drone.y += dy

        drone.battery -= 0.5

    @staticmethod
    def recharge(drone: DroneEntity):

        drone.battery = 100.0
