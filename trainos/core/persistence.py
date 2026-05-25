import json
from pathlib import Path
from datetime import datetime


class PersistenceManager:

    def __init__(self):
        self.save_dir = Path("trainos/data/saves")
        self.snapshot_dir = Path("trainos/data/snapshots")
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)

    def save_world(self, state: dict):
        path = self.save_dir / "world.json"
        with open(path, "w") as file:
            json.dump(state, file, indent=2)

    def load_world(self):
        path = self.save_dir / "world.json"
        if not path.exists():
            return {}
        with open(path, "r") as file:
            return json.load(file)

    def snapshot(self, state: dict):
        timestamp = datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
        path = self.snapshot_dir / f"snapshot_{timestamp}.json"
        with open(path, "w") as file:
            json.dump(state, file, indent=2)
