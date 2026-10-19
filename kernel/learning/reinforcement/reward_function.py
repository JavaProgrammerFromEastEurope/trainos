from .reward import Reward


class RewardFunction:

    def compute(
        self,
        value: float,
    ) -> Reward:
        return Reward(value=value)
