class Wagon:

    def __init__(self, wagon_id):
        self.wagon_id = wagon_id
        #
        # Sector storage
        #
        self.sectors = {}

    def add_sector(self, sector):
        self.sectors[sector.sector_id] = sector

    def get_sector(self, sector_id):
        return self.sectors.get(sector_id)
