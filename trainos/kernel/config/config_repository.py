# kernel/config/config_repository.py

from __future__ import annotations
from trainos.kernel.config.config_schema import ConfigSchema


class ConfigRepository:

    def __init__(self) -> None:
        self._schema = ConfigSchema()

    def set(
        self,
        key: str,
        value: object,
    ) -> None:

        self._schema.values[key] = value

    def get(
        self,
        key: str,
        default: object | None = None,
    ) -> object | None:
        return self._schema.values.get(key, default)

    def has(self, key: str) -> bool:
        return key in self._schema.values

    def remove(self, key: str) -> None:
        self._schema.values.pop(key, None)

    def clear(self) -> None:
        self._schema.values.clear()

    def export(self) -> dict[str, object]:
        return dict(self._schema.values)


