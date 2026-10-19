from .constitutional_rollback import ConstitutionalRollback


class RollbackEngine:

    def rollback(
        self,
        rollback: ConstitutionalRollback,
    ) -> ConstitutionalRollback:
        return rollback