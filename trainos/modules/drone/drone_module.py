from trainos.core.module import BaseModule
from trainos.core.events import Event

from trainos.modules.drone.drone_entity import DroneEntity
from trainos.modules.drone.drone_manager import DroneManager
from trainos.modules.drone.drone_commands import DroneCommands


class DroneModule(BaseModule):

    def __init__(self, event_bus, telemetry):

        super().__init__("drone_module", event_bus, telemetry)

        self.manager = DroneManager()

    def start(self):

        self.telemetry.log("Drone module started")

        drone = DroneEntity(drone_id="drone_001")

        self.manager.register(drone)

        self.event_bus.subscribe("MOVE_DRONE", self.on_move_drone)

    def on_move_drone(self, event: Event):

        drone_id = event.payload["drone_id"]

        dx = event.payload["dx"]
        dy = event.payload["dy"]

        drone = self.manager.get(drone_id)

        if drone:

            DroneCommands.move(drone, dx, dy)

            self.telemetry.metric(f"drone.{drone_id}.battery", drone.battery)

    def update(self):

        self.event_bus.publish(
            Event(
                type="MOVE_DRONE", payload={"drone_id": "drone_001", "dx": 1, "dy": 0}
            )
        )

        for drone in self.manager.all():

            print(
                f"[DRONE] "
                f"{drone.drone_id} "
                f"POS=({drone.x}, {drone.y}) "
                f"BAT={drone.battery}"
            )

    def shutdown(self):

        self.telemetry.log("Drone module shutdown")
