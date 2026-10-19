from .transfer_route import TransferRoute


class LogisticsEngine:

    def plan_route(self) -> TransferRoute:
        return TransferRoute(path=["A", "B", "C"])
