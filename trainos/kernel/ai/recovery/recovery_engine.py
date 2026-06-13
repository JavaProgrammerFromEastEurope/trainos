from __future__ import annotations

from .recovery_policy 	import RecoveryPolicy
from .retry_manager 		import RetryManager
from .retry_state 			import RetryState
from .rollback_manager 	import RollbackManager
from .recovery_result 	import RecoveryResult


class RecoveryEngine:

    def __init__(self) -> None:
        self._retry_manager 		= RetryManager()
        self._rollback_manager 	= RollbackManager()

    def recover(
        self,
        retry_state: RetryState,
        policy: RecoveryPolicy,
        completed_nodes: list[str],
    ) -> RecoveryResult:
        if self._retry_manager.should_retry(
            retry_state,
            policy,
        ):
            retry_state.increment()
            return RecoveryResult(
                recovered=True,
                rolled_back=False,
                retry_count=retry_state.attempts,
            )
        if policy.rollback_on_failure:
            self._rollback_manager.rollback(
                completed_nodes,
            )
            return RecoveryResult(
                recovered=False,
                rolled_back=True,
                retry_count=retry_state.attempts,
            )
        return RecoveryResult(
            recovered=False,
            rolled_back=False,
            retry_count=retry_state.attempts,
        )
