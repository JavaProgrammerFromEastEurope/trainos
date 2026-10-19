class RewardMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_reward = 0.0

    def add(
        self,
        reward: float,
    ) -> None:
        self.total_reward += reward
