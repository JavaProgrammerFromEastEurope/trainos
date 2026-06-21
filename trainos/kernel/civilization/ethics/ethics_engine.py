from .ethics import Ethics
from .ethics_type import EthicsType


class EthicsEngine:

    def evaluate(self) -> Ethics:
        return Ethics(
            type=EthicsType.COOPERATIVE,
        )
