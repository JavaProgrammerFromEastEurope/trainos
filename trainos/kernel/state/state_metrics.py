from __future__ import annotations


class StateMetrics:

    def __init__(self) -> None:
        self.key_count: 		int = 0
        self.change_count: 	int = 0
        self.watcher_count: int = 0
        self.transaction_count: int = 0
        self.history_size: 	int = 0
        self.tick_count: 		int = 0

    def snapshot(self) -> dict[str, int]:
        return {
            "key_count": 			self.key_count,
            "change_count": 	self.change_count,
            "watcher_count": 	self.watcher_count,
            "transaction_count": self.transaction_count,
            "history_size": 	self.history_size,
            "tick_count": 		self.tick_count,
        }
