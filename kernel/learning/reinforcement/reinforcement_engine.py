from .reinforcement_result import ReinforcementResult


class ReinforcementEngine:

    def train(self) -> ReinforcementResult:
        return ReinforcementResult(improved=True)
