class OccupancyMap:

    def __init__(self):
        self.occupied = {}

    def clear(self):
        self.occupied.clear()

    def occupy(self, x, y, entity_id):
        self.occupied[(x, y)] = entity_id

    def release(self, x, y):
        self.occupied.pop((x, y), None)

    def is_occupied(self, x, y):
        return (x, y) in self.occupied

    def get_entity(self, x, y):
        return self.occupied.get((x, y))
