from trainos.modules.drone.drone_entity import DroneEntity


class DroneCommands(DroneEntity):

    @staticmethod
    def move(
      drone: DroneEntity,
      dx: float,
      dy: float):

        if not drone.active:
            return

        if drone.battery <= 0:
            return

        movement_cost = 0.5

        if drone.battery < movement_cost:
            return

        drone.x += dx
        drone.y += dy

        if drone.x < 0:
            return

        if drone.y > 100:
            return

        drone.battery -= movement_cost
