from __future__ import annotations

import json
from typing import Any


class StateSerializer:

    def serialize(self, state: dict[str, Any]) -> str:
        return json.dumps(
            state,
            ensure_ascii=False,
        )

    def deserialize(self, data: str) -> dict[str, Any]:
        return json.loads(data)
