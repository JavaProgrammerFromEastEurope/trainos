class AnomalyMemory:

    def __init__(self):
        self.repeat_leaks = {}

    def register_leak(self, sector_id):
        self.repeat_leaks[sector_id] = self.repeat_leaks.get(sector_id, 0) + 1

    def is_hotspot(self, sector_id):
        return self.repeat_leaks.get(sector_id, 0) > 3
