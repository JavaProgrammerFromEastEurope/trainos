class WorldGrid:

    def __init__(self):
        #
        # Wagons storage
        #
        self.wagons = {}

    def add_wagon(self, wagon):
        self.wagons[wagon.wagon_id] = wagon

    def get_wagon(self, wagon_id):
        return self.wagons.get(wagon_id)

    def get_sector(self, wagon_id, sector_id):
        #
        # FIND WAGON
        #
        wagon = self.get_wagon(wagon_id)
        if not wagon:
            return None
        #
        # FIND SECTOR
        #
        return wagon.get_sector(sector_id)
