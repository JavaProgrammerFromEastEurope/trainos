class WorldStateCache:

    def __init__(self):
        self.cache = {}

    def update(self, snapshot):
        self.cache["snapshot"] = snapshot

    def get(self):
        return self.cache.get("snapshot")