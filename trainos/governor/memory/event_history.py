from collections import deque
from time import time


class EventHistory:

    def __init__(self, max_size=500):
        self.events = deque(maxlen=max_size)

    def add(self, event_type, sector_id, meta=None):
        self.events.append(
            {
                "t": time(),
                "type": event_type,
                "sector_id": sector_id,
                "meta": meta or {},
            }
        )

    def recent(self, event_type, sector_id, window=30):
        now = time()
        return [
            e
            for e in self.events
            if e["type"] == event_type
            and e["sector_id"] == sector_id
            and (now - e["t"]) < window
        ]
