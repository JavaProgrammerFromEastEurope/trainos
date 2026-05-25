class Wagon:

    def __init__(self, wagon_id: str):
        self.wagon_id = wagon_id
        self.sectors = {}

    def add_sector(self, sector):
        self.sectors[sector.sector_id] = sector
