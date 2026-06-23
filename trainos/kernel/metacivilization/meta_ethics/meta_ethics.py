from dataclasses import dataclass

from .meta_ethics_type import MetaEthicsType


@dataclass
class MetaEthics:

    type: MetaEthicsType
