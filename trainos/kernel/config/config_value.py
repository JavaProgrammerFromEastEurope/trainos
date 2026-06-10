# kernel/config/config_value.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ConfigValue:
    key: str
    value: Any
