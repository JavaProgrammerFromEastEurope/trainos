from dataclasses import dataclass

from .ethics_type import EthicsType


@dataclass
class Ethics:
    type: EthicsType