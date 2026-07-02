from .constitutional_history import ConstitutionalHistory


class HistoryEngine:

    def snapshot(
        self,
        history: ConstitutionalHistory,
    ) -> ConstitutionalHistory:
        return history