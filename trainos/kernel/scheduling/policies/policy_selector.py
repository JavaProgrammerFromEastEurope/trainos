from .scheduler_policy import SchedulerPolicy


class PolicySelector:

    def select(
        self,
        policy: SchedulerPolicy,
    ) -> SchedulerPolicy:
        return policy
