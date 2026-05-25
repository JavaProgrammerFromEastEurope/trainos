from pathlib import Path

import yaml


class ConfigLoader:

    def __init__(self, config_dir="trainos/configs"):

        self.config_dir = Path(config_dir)

        self.cache = {}

    def load(self, filename: str):

        if filename in self.cache:
            return self.cache[filename]

        path = self.config_dir / filename

        with open(path, "r") as file:

            data = yaml.safe_load(file)

        self.cache[filename] = data

        return data
