import time

class TickLoop:

    def __init__(self, tick_rate: int = 60):
        self.tick_rate = tick_rate
        self.fixed_delta = 1.0 / tick_rate
        self.running = False

    def run(self, callback):
        self.running = True
        previous_time = time.perf_counter()
        accumulator = 0.0

        while self.running:
            current_time = time.perf_counter()
            frame_time = current_time - previous_time
            previous_time = current_time
            accumulator += frame_time
            while accumulator >= self.fixed_delta:
                callback()
                accumulator -= self.fixed_delta
            time.sleep(0.001)

    def stop(self):
        self.running = False
