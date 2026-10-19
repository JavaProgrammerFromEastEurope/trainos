from .citizen_lifecycle import CitizenLifecycle


class LifecycleEngine:

    def transition(
        self,
        lifecycle: CitizenLifecycle,
    ) -> CitizenLifecycle:
        return lifecycle