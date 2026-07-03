from dataclasses import dataclass


@dataclass(frozen=True)
class RegistryPolicy:

    allow_overwrite: 	bool
    immutable_keys: 	bool