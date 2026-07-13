from dataclasses import dataclass

from .runtime_snapshot import RuntimeSnapshot
from .profile_snapshot import ProfileSnapshot
from .value_snapshot import ValueSnapshot


@dataclass(frozen=True, slots=True)
class ConfigurationSnapshot:

    snapshot_id: str
    runtime: 	RuntimeSnapshot
    profile: 	ProfileSnapshot
    values: 	ValueSnapshot