from .base_history_registry import BaseHistoryRegistry


class HistoryQuery:

    def latest(self, registry: BaseHistoryRegistry):
        return registry.latest()

    def all(self, registry: BaseHistoryRegistry):
        return registry.all()
