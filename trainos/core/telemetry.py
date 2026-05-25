from collections import defaultdict
from datetime import datetime


class Telemetry:

    def __init__(self):

        self.metrics = defaultdict(list)
        self.logs = []

    def metric(self, name: str, value):

        self.metrics[name].append(
          {"timestamp": datetime.utcnow(),
          "value": value})

    def log(self, message: str):

        self.logs.append(
          {"timestamp": datetime.utcnow(),
            "message": message})

        print(f"[LOG] {message}")
