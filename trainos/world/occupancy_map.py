class OccupancyMap:

    def __init__(self, world=None):
        #
        # RUNTIME ENTITY OCCUPATION
        # {(x, y): entity_id}
        #

        self.occupied = {}
        #
        # WORLD REFERENCE
        #
        self.world = world
    #
    # CLEAR ALL OCCUPIED CELLS
    #
    def clear(self):
        self.occupied.clear()
    #
    # MARK CELL OCCUPIED
    #
    def occupy(self, x, y, entity_id):
        self.occupied[(x, y)] = entity_id
    #
    # RELEASE CELL
    #
    def release(self, x, y):
        self.occupied.pop((x, y), None)
    #
    # CHECK OCCUPATION
    #
    def is_occupied(self, x, y):
        return (x, y) in self.occupied
    #
    # GET ENTITY IN CELL
    #
    def get_entity(self, x, y):
        return self.occupied.get((x, y))
    #
    # BUILD WALKABLE SET FOR A*
    #
    def get_walkable_set(
        self,
        wagon_id,
        sector_id,
    ):
        #
        # WORLD REQUIRED
        #
        if self.world is None:
            return set()

        wagon = self.world.get_wagon(wagon_id)

        if not wagon:
            return set()

        sector = wagon.sectors.get(sector_id)

        if not sector:
            return set()

        walkable = set()
        #
        # SCAN ALL CELLS
        #
        for (x, y), cell in sector.cells.items():
            #
            # STATIC WALL CHECK
            #
            if not cell.walkable:
                continue
            #
            # DYNAMIC OCCUPATION CHECK
            #
            if self.is_occupied(x, y):
                continue
            walkable.add((x, y))
        return walkable
