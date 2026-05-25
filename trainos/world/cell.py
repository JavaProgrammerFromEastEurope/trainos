from dataclasses import dataclass

@dataclass(slots=True)
class WorldCell:

    x: int
    y: int

    walkable: 		bool 	= True
    oxygen: 			float = 100.0
    pressure: 		float = 1.0
    temperature: 	float = 20.0
