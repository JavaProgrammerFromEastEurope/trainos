from trainos.world.cell import WorldCell


class Sector:
    def __init__(self, sector_id: str, width: int, height: int):
        self.sector_id = sector_id
        self.width = width
        self.height = height
        self.cells = {}

    def generate(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[(x, y)] = WorldCell(x = x, y = y)

    def get_cell(self, x, y):
        return self.cells.get((x, y))
