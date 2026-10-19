from .trade_result import (
    TradeResult,
)


class TradeEngine:

    def execute(self) -> TradeResult:
        return TradeResult(success=True)
