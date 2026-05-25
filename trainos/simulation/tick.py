import time


class TickLoop:

    def __init__(self, tick_rate: float = 1.0):
        self.tick_rate = tick_rate
        self.running = False

    def run(self, callback):

        self.running = True

        while self.running:

            callback()

            time.sleep(self.tick_rate)

    def stop(self):
        self.running = False
