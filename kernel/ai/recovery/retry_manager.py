from __future__ import annotations

from .retry_state 		import RetryState
from .recovery_policy import RecoveryPolicy


class RetryManager:

    def should_retry(
        self,
        state: RetryState,
        policy: RecoveryPolicy,
    ) -> bool:
        return (
            state.attempts
            < policy.max_retries
        )