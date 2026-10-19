from .economic_history_registry import EconomicHistoryRegistry


class HistoryQuery:

    def latest(
        self,
        registry: EconomicHistoryRegistry,
    ):
        entries = registry.entries()
        if not entries:
            return None
        return entries[-1]
