from .meta_ethics import MetaEthics
from .meta_ethics_type import MetaEthicsType


class MetaEthicsEngine:

    def evaluate(self) -> MetaEthics:
        return MetaEthics(type=MetaEthicsType.ADAPTIVE)
