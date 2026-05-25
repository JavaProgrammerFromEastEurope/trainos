class SimulationClock:

    def __init__(self, tick_rate: int = 60):
        self.tick_rate 				= tick_rate
        self.tick 						= 0
        self.simulation_time 	= 0.0
        self.delta_time 			= 1.0 / tick_rate

    def step(self):
        self.tick += 1
        self.simulation_time += self.delta_time

    def current_tick(self):
        return self.tick
