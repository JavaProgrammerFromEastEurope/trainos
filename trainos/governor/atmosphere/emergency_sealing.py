class EmergencySealing:

    def __init__(self, world):
        self.world = world

    def seal_sector(self, sector_id: int):
        sector = self.world.sectors[sector_id]
        sector.sealed = True

    def unseal_sector(self, sector_id: int):
        sector = self.world.sectors[sector_id]
        sector.sealed = False