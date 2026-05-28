from trainos.modules.drone.drone_entity import DroneEntity


class DroneManager:

    def __init__(self):
        self.drones: dict[str, DroneEntity] = {}

    def register(self, drone: DroneEntity):
        self.drones[drone.drone_id] = drone

    def get(self, drone_id: str):
        return self.drones.get(drone_id)

    def all(self):
        return self.drones.values()
