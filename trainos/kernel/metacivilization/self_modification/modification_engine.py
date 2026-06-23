from .modification_event import ModificationEvent


class ModificationEngine:

    def apply(self, event: ModificationEvent) -> ModificationEvent:
        return ModificationEvent(
            source=event.source,
            target_system=event.target_system,
            change_description=f"applied: {event.change_description}",
        )
