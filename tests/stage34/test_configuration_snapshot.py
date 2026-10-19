from kernel.configuration.snapshot.configuration_snapshot import ConfigurationSnapshot

from kernel.configuration.snapshot.runtime_snapshot import RuntimeSnapshot
from kernel.configuration.snapshot.profile_snapshot import ProfileSnapshot
from kernel.configuration.snapshot.value_snapshot 	import ValueSnapshot
from kernel.configuration.snapshot.snapshot_engine 	import SnapshotEngine
from kernel.configuration.runtime.runtime_status 		import ConfigurationRuntimeStatus


def test_configuration_snapshot():

    snapshot = ConfigurationSnapshot(
        snapshot_id="SNAP1",
        runtime=RuntimeSnapshot(
            runtime_id="CFG1",
            status=ConfigurationRuntimeStatus.RUNNING,
        ),
        profile=ProfileSnapshot(
            active_profile="Production",
        ),
        values=ValueSnapshot(value_count=128),
    )

    result = SnapshotEngine().capture(snapshot)
    assert result.snapshot_id == "SNAP1"
    assert result.profile.active_profile == "Production"
    assert result.values.value_count == 128
