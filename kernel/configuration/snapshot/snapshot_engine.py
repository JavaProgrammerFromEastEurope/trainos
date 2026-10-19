from .configuration_snapshot import ConfigurationSnapshot


class SnapshotEngine:

    def capture(
        self,
        snapshot: ConfigurationSnapshot,
    ) -> ConfigurationSnapshot:
        return snapshot
