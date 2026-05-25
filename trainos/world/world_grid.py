from trainos.world.wagon import Wagon


class WorldGrid:

    def __init__(self):
        self.wagons = {}

    def add_wagon(self, wagon: Wagon):
        self.wagons[wagon.wagon_id] = wagon

    def get_wagon(self, wagon_id: str):
        return self.wagons.get(wagon_id)
