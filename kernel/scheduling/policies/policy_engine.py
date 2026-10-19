from .policy_selector import PolicySelector


class PolicyEngine:

    def __init__(self):
        self.selector = PolicySelector()

    def select(
        self,
        policy,
    ):
        return self.selector.select(policy)
