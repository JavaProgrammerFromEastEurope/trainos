from dataclasses import dataclass

from .adapter_type import AdapterType


@dataclass(frozen=True, slots=True)
class IntegrationAdapter:

    adapter_id: str
    adapter_type: AdapterType