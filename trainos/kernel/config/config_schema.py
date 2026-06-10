# kernel/config/config_schema.py

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class ConfigSchema:
    values: dict[str, object] = field(default_factory=dict)
