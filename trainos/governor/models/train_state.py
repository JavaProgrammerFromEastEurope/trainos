from dataclasses import dataclass


@dataclass
class TrainState:

    tick: 						int
    total_entities: 	int
    active_entities: 	int
    total_tasks: 			int
    active_tasks: 		int
    idle_drones: 			int
    busy_drones: 			int
    average_battery: 	float
    congestion: 			float
    emergency_level: 	float
